# Binary Scanning Tool
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

The binary scanning tool is a demo for using a machine learning model to solve the 
binary function recognition task, i.e. recognize a binary function (compiled with 
different compilers, processor architectures, optimization levels) from a set of 
known functions. 

We demonstrate a application for known-vulnerability scanning by combining a vector 
database ([ChromaDB](https://github.com/chroma-core/chroma)) with a very basic 
disassembly tool. The process works like this:
1) Load the database and the machine learning model
2) Run a disassembly pass on all functions contained within the binary file 
3) Infer the embedding vectors of the binary functions by passing them through 
our embedding model
4) Lookup the `K` nearest vectors of functions contained in our database 
5) If any of these functions is flagged as 'vulnerable' (with an CVE number), reject 
the binary.

## Dependencies
As referenced by `requirements.txt`:
- capstone
- chromadb
- click
- pyelftools
- tabulate
- transformers
- optimum[onnxruntime] (*note*: Providing a GPU reduces the inference time x10)

## Running
In the most simple scenario:
`$ python disassemble.py check --model clap-onnx/ --database chroma/ <binary-file>`
The script returns `0 (EXIT_SUCCESS)` if **no** vulnerable functions where identified.

## SaaS 
Scanning as a Service (SaaS) is implemented through `hosted.py`.

## Demo
For the demo, we provide two binary files. They are compiled from the same source code,
but are statically linked to different versions of the OpenSSL library:
- b64_good: OpenSSL 3.0.15-1
- b64_bad: OpenSSL_1.0.2d

**Important**: The b64_bad deliberately contains a vulnerable version of the `EVP_EncodeUpdate`
function (ref. CVE-2016-2105).

The included `chroma`-database contains embeddings for library functions contained 
within various versions of the OpenSSL library.
