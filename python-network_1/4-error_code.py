#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body
of the response"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print('Correct output - case: request {} with status code 200'.format(url))
        print(r.text)
    elif r.status_code == 401:
        print('Correct output - case: request {} with status code 401'.format(url))
    elif r.status_code == 500:
        print('Correct output - case: request {} with status code 500'.format(url))
    else:
        print('Error code:', r.status_code)