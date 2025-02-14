#!/usr/bin/env python3
# GNU Lesser General Public License v3.0 or later
# @author Dominik Bayerl <dominik.bayerl@carissma.eu>
import argparse
import hashlib
import io
import itertools
import json
import logging
import os
import queue
import threading
import time

import chromadb
from capstone import *
from elftools.elf.elffile import ELFFile, SymbolTableSection
from flask import Flask, jsonify, request, send_from_directory
from pipelines import pipeline

app = Flask(__name__)

# Create a priority queue for processing ELF files
task_queue = queue.PriorityQueue()

# Database connection
chroma_client = chromadb.HttpClient(
    host=os.environ.get("CHROMA_HOST", "http://localhost:8000")
)

# Directory to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class Disassembler:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.md = Cs(*args, **kwargs)

    def __call__(self, stream: io.IOBase):
        elf = ELFFile(stream)
        symtab = next(
            section
            for section in elf.iter_sections()
            if isinstance(section, SymbolTableSection)
        )
        if not symtab:
            raise ValueError("No symbol table found in the ELF file.")
        text = elf.get_section_by_name(".text")
        if not text:
            raise ValueError("No .text section found in the ELF file.")

        ops = text.data()
        base_addr = text["sh_addr"]

        for symbol in symtab.iter_symbols():
            if symbol["st_info"]["type"] == "STT_FUNC":
                func_name = symbol.name
                func_addr = symbol["st_value"]
                func_size = symbol["st_size"]
                if func_size > 0:
                    offset = func_addr - base_addr
                    func_data = ops[offset : offset + func_size]
                    yield {
                        "name": func_name,
                        "addr": func_addr,
                        "size": func_size,
                        "instructions": {
                            i.address: (i.mnemonic + " " + i.op_str).strip()
                            for i in self.md.disasm(func_data, func_addr)
                        },
                    }


# Hashing function (default: blake2b)
def calculate_hash(data, algorithm="blake2b", **kwargs):
    hash_func = getattr(hashlib, algorithm, hashlib.blake2b)(**kwargs)
    hash_func.update(data)
    return hash_func.hexdigest()


def task_runner(model=None, trust_remote_code=False, **kwargs):
    dism = Disassembler(CS_ARCH_X86, CS_MODE_64)
    pipe = pipeline("binary-function-recognition", model=model, trust_remote_code=trust_remote_code)
    collection = chroma_client.get_collection("functions")

    def run(fd: io.IOBase):
        functions = list(dism(fd))
        inputs = [f for f in functions if len(f["instructions"]) >= 100]

        # Debugging
        if app.debug:
            inputs = inputs[:5]

        vectors = [tensor.tolist() for tensor in pipe(inputs)]
        hits = collection.query(
            query_embeddings=vectors, n_results=5, include=["metadatas", "distances"]
        )
        results = []
        for f, gs, ds in zip(inputs, hits["metadatas"], hits["distances"]):
            MAX_DISTANCE = 0.46
            matches = [(g, d) for g, d in zip(gs, ds) if d < MAX_DISTANCE]
            if len(matches) > 0:
                gs, ds = zip(*matches)
            else:
                gs, ds = [], []
            results.append(
                {
                    "name": f["name"],
                    "functions": gs,
                    "distances": ds,
                }
            )
        return results

    while True:
        priority, filename = task_queue.get()

        app.logger.info(f"Processing {filename} with priority {priority}")
        try:
            with open(filename, "rb") as fd:
                result = run(fd)
            status = (
                "success"
                if not any(g["cve"] for f in result for g in f["functions"])
                else "fail"
            )
            response = {"status": status, "data": result}
        except Exception as e:
            app.logger.error(f"Error processing {filename}: {e}")
            response = {"status": "error", "data": e}
        
        base, _ = os.path.splitext(os.path.basename(filename))
        with open(os.path.join(UPLOAD_FOLDER, base + '.json'), 'w') as fd:
            json.dump(response, fd)
        app.logger.info(f"Finished processing {filename}")
        app.logger.debug(f"\t{response}")

        task_queue.task_done()

@app.route("/", methods=["POST"])
def upload_file():
    if request.content_type != "application/octet-stream":
        return (
            jsonify(
                {
                    "status": "fail",
                    "data": {
                        "error": "Invalid content type, expected application/octet-stream"
                    },
                }
            ),
            400,
        )

    priority = int(request.headers.get("Priority", 1))  # Default priority is 1

    # Compute hash before writing file
    file_hash = calculate_hash(request.data, algorithm="blake2b", digest_size=20)
    filepath = os.path.join(UPLOAD_FOLDER, f"{file_hash}.bin")

    # Save the file
    with open(filepath, "wb") as f:
        f.write(request.data)

    # Add to processing queue
    queue_position = task_queue.qsize()
    task_queue.put((priority, filepath))

    return jsonify(
        {
            "status": "success",
            "data": {
                "hash": file_hash,
                "priority": priority,
                "queue_position": queue_position,
            },
        }
    )

@app.route('/<hash>', methods=['GET'])
def send_report(hash):
    return send_from_directory(UPLOAD_FOLDER, hash)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the binary scan hosted service.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--model", type=str, help="Model ID for inference")
    parser.add_argument("--trust-remote-code", action="store_true", help="Enable loading of remote models")
    trust_remote_code=True
    args = parser.parse_args()

    app.logger.setLevel(logging.INFO)
    if args.debug:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
    
    # Start a background thread for processing
    threading.Thread(target=task_runner, kwargs=vars(args), daemon=True).start()

    app.run()
