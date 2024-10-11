#!/usr/bin/env python
import os.path
import dotenv
import requests
import urllib3

RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
LIGHT_CYAN = "\033[1;36m"
END = "\033[0m"

ELASTIC_PASSWORD = dotenv.get_key(dotenv_path="../.env", key_to_get="ELASTIC_PASSWORD")
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)


def main():
    try:
        print(f"{CYAN}What would you like to do?\nOptions: {LIGHT_CYAN}[dump | upload | quit]")
        user_in: str = input()
        if user_in.lower().startswith("q"):
            exit(0)
        if user_in.lower() == "dump":
            dump()
        elif user_in.lower() == "upload":
            upload()
        else:
            print(f"{RED}Unknown option{END}")
    except KeyboardInterrupt:
        print(f"{END}")
        exit(0)


def dump() -> None:
    print(f"{CYAN}What is the name of the index?{LIGHT_CYAN}")
    index: str = input()
    if not index_exists(index):
        print(f"{RED}Specified index doesn't exist")
        return
    print(f"{CYAN}Where should the dumped data be stored? (e.g. index.json){LIGHT_CYAN}")
    file_name: str = input()
    validate_index_and_filename(index, file_name)
    host: str = f"https://elastic:{ELASTIC_PASSWORD}@localhost:9200/{index}"
    print(f"{GREEN}Starting index dump...{END}")
    os.system(f"NODE_TLS_REJECT_UNAUTHORIZED=0 elasticdump --input={host} --output={file_name} --type=data")


def upload() -> None:
    print(f"{CYAN}What should the index be called?{LIGHT_CYAN}")
    index: str = input()
    if index_exists(index):
        print(f"{YELLOW}Warning: an index named {index} already exists. Continue? [y/n]{LIGHT_CYAN}")
        answer: str = input()
        if not answer.lower().startswith("y"):
            print(f"{END}")
            return
    print(f"{CYAN}What is the name of the dumped index file?{LIGHT_CYAN}")
    file_name: str = input()
    validate_index_and_filename(index, file_name)
    if not os.path.isfile(file_name):
        print(f"{RED}Specified file doesn't exist")
        return
    host: str = f"https://elastic:{ELASTIC_PASSWORD}@localhost:9200/{index}"
    print(f"{GREEN}Starting index upload...{END}")
    os.system(f"NODE_TLS_REJECT_UNAUTHORIZED=0 elasticdump --input={file_name} --output={host} --type=data")


def validate_index_and_filename(index: str, file_name: str) -> None:
    if len(index) == 0 or len(file_name) == 0:
        print(f"{RED}Invalid filename or index{END}")
        exit(-1)


def index_exists(index: str) -> bool:
    return requests.head(f"https://elastic:{ELASTIC_PASSWORD}@localhost:9200/{index}", verify=False).status_code != 404


if __name__ == "__main__":
    main()
