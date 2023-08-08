#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests
import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.getheader("X-Request-Id"))
        print("Please provide a URL as a command-line argument")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(f"X-Request-Id: {request_id}")