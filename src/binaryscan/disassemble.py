#!/usr/bin/env python3
# GNU Lesser General Public License v3.0 or later
# @author Dominik Bayerl <dominik.bayerl@carissma.eu>


import sys
import click
import json
from capstone import *
from elftools.elf.elffile import ELFFile
from chromadb import PersistentClient
from tabulate import tabulate
from model import ONNX_Runtime, rebase

ARCH_OPTIONS = {
    "x86": (CS_ARCH_X86, CS_MODE_32),
    "x86_64": (CS_ARCH_X86, CS_MODE_64),
    "arm": (CS_ARCH_ARM, CS_MODE_ARM),
    "arm_thumb": (CS_ARCH_ARM, CS_MODE_THUMB),
    "aarch64": (CS_ARCH_ARM64, CS_MODE_ARM),
    "mips": (CS_ARCH_MIPS, CS_MODE_MIPS32),
}


def get_functions(binary):
    """
    Extracts the functions from the ELF binary.
    Returns a list of dictionaries with function name, address, and size.
    """
    functions = []
    with open(binary, "rb") as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name(".symtab")

        if not symtab:
            raise ValueError("No symbol table found in the ELF file.")

        for symbol in symtab.iter_symbols():
            if symbol["st_info"]["type"] == "STT_FUNC":
                func_name = symbol.name
                func_addr = symbol["st_value"]
                func_size = symbol["st_size"]
                if func_size > 0:
                    functions.append(
                        {"name": func_name, "address": func_addr, "size": func_size}
                    )
    return functions


def list_functions_impl(binary):
    """
    Implementation of listing functions in a binary.
    """
    functions = get_functions(binary)
    result = []
    for func in functions:
        result.append(
            f"{func['name']:30}  0x{func['address']:08x}  {func['size']} bytes"
        )
    return result


def disassemble_impl(binary, arch, function=None):
    """
    Implementation of disassembling functions in a binary.
    """
    arch = arch.lower()
    if arch not in ARCH_OPTIONS:
        raise ValueError(f"Unsupported architecture: {arch}")
    cs_arch, cs_mode = ARCH_OPTIONS[arch]

    with open(binary, "rb") as f:
        elf = ELFFile(f)
        text_section = elf.get_section_by_name(".text")
        if not text_section:
            raise ValueError("No .text section found in the ELF file.")

        text_data = text_section.data()
        text_addr = text_section["sh_addr"]

        md = Cs(cs_arch, cs_mode)
        functions = get_functions(binary)

        result = {}

        if function:
            functions = list(filter(lambda f: f["name"] == function, functions))
            if len(functions) < 1:
                raise ValueError(f"Function '{function}' not found in the binary.")

        # Disassemble functions
        for func in functions:
            offset = func["address"] - text_addr
            func_bytes = text_data[offset : offset + func["size"]]
            result[func["name"]] = list(md.disasm(func_bytes, func["address"]))

        return result


@click.group()
def cli():
    """A tool for analyzing ELF binaries."""
    pass


@cli.command()
@click.argument("binary", type=click.Path(exists=True, dir_okay=False, readable=True))
def list_functions(binary):
    """
    List all functions in the provided ELF binary.
    """
    try:
        results = list_functions_impl(binary)
        click.echo("\n".join(results))
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument("binary", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option(
    "--arch",
    type=click.Choice(ARCH_OPTIONS.keys(), case_sensitive=False),
    default="x86_64",
    help="Architecture to use for disassembly.",
)
@click.option(
    "--function",
    type=str,
    default=None,
    help="Name of the specific function to disassemble.",
)
@click.option(
    "--out",
    type=click.Path(writable=True),
    default=None,
    help="File for disassembly output."
)
def disassemble(binary, arch, function, out):
    """
    Disassemble the specified function (or all functions if no name is provided) in the ELF binary.
    """
    results = disassemble_impl(binary, arch, function)
    asm = {}
    for func, instructions in results.items():
        if len(instructions) < 1:
            continue

        ea = instructions[0].address
        click.echo(f"Function: {func} at 0x{ea:08x}")
        click.echo(
            "\n".join(
                f"0x{instr.address:x}:\t{instr.mnemonic}\t{instr.op_str}"
                for instr in instructions
            )
        )

        asm_dict = {
            instr.address: f"{instr.mnemonic}\t{instr.op_str}".strip() for instr in instructions
        }
        result = rebase(asm_dict)
        click.echo(result)
        asm[func] = result

    with open(out, "w", encoding="utf8") as fp:
        json.dump(asm, fp)


@cli.command()
@click.argument("binary", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option(
    "--threshold",
    type=float,
    default=0.2,
    show_default=True,
    help="Maximum distance for a match. Balances False-Positives vs. False-Negatives.",
)
@click.option(
    "--database", type=str, default="./chroma", required=True, help="Server address."
)
@click.option(
    "--model",
    type=click.Path(exists=True, dir_okay=True, readable=True),
    required=True,
    help="Path to the model file.",
)
@click.option(
    "--min",
    "min_value",
    type=int,
    default=10,
    show_default=True,
    help="Minimum function length (number of instructions).",
)
@click.option(
    "--top_k",
    type=int,
    default=3,
    show_default=True,
    help="Number of candidates to query",
)
def check(binary, threshold, database, model, min_value, top_k):
    """
    Check command scaffold.
    """
    click.echo(
        f"Running 'check' with threshold={threshold}, database={database}, model={model}, min={min_value}"
    )

    click.echo("Loading model...")
    load_args = {"trust_remote_code": True}  # remove for remote sources
    model = ONNX_Runtime(model, model_kwargs=load_args, tokenizer_kwargs=load_args)

    click.echo("Opening database...")
    client = PersistentClient(database)
    col = client.get_collection("functions", embedding_function=model)

    click.echo("Disassembling binary...")
    functions = disassemble_impl(binary, arch="x86_64")
    functions = {k: v for k, v in functions.items() if len(v) >= min_value}

    rebased_asm = []
    for name, instructions in functions.items():
        asm_dict = {
            instr.address: f"{instr.mnemonic}\t{instr.op_str}" for instr in instructions
        }
        rebased_asm.append(rebase(asm_dict))

    click.echo(f"Running inference on {len(functions)} functions...")
    embeddings = model(rebased_asm)

    click.echo("Querying database...")
    results = col.query(
        query_embeddings=embeddings,
        n_results=top_k,
        include=["metadatas", "distances"],
    )

    click.echo("\nResults")
    table = []
    ret_code = 0
    headers = ["Function", *[f"Match {i+1}" for i in range(top_k)], "Verdict"]
    for func, meta, dist in zip(
        functions.keys(), results["metadatas"], results["distances"]
    ):
        verdict = next(
            (
                m.get("cve")
                for m, d in zip(meta, dist)
                if d <= threshold and m.get("cve") is not None
            ),
            "Not Guilty",
        )
        ret_code = -1 if verdict != "Not Guilty" else ret_code

        row = [
            func,
            *[f"{m['func_name']} ({d:.03f}) " for m, d in zip(meta, dist)],
            verdict,
        ]
        table.append(row)
    click.echo(tabulate(table, headers))
    sys.exit(ret_code)

if __name__ == "__main__":
    cli()
