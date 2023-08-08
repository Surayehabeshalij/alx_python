#!/usr/bin/python3
"""takes letter and sends a POST req to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
import sys


if __name__ == '__main__':
    letter = {'q': sys.argv[1][0] if len(sys.argv) > 1 else ''}
    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        response = r.json()
        if response:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')