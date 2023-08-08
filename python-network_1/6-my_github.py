#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""
import requests
import sys 


if __name__ == '__main__':
    r = requests.get('https://api.github.com/Surayehabeshalij', auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        print('Not a valid JSON')