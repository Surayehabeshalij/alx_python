#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))