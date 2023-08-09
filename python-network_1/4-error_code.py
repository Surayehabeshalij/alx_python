#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
import requests
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)