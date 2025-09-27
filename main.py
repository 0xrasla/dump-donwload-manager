import json
import requests
import sys
import re

ARIA2_RPC = "http://localhost:6800/jsonrpc"

url_pattern = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"


def validate_url(url):
    return re.fullmatch(url_pattern, url)


def add_download(url):
    payload = {
        "jsonrpc": "2.0",
        "method": "aria2.addUri",
        "id": "bro",
        "params": [[url]],
    }
    res = requests.post(ARIA2_RPC, json=payload)
    return res.json()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)

    url = sys.argv[1] if validate_url(sys.argv[1]) else ""
    if url:
        response = add_download(url)
    else:
        print("Info: provide a valid url.")
