#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage:  <URL>
"""
import requests
import sys

def retrieve_x_request_id(url):
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f'The value of X-Request-Id is: {x_request_id}')
        else:
            print('X-Request-Id header not found in the response.')
    except requests.exceptions.RequestException as e:
        print(f'An error occurredd: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a URL as an argument.')
        sys.exit(1)

    url = sys.argv[1]
    retrieve_x_request_id(url)
