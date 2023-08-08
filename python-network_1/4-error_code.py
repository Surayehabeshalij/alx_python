#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body
of the response"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a URL as a command-line argument")
        sys.exit(1)

    url = sys.argv[1]
    r = requests.get(url)
    
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)