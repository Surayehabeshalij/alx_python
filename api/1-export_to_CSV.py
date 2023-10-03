#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

def user_info(user_id):
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if user_response.status_code != 200:
        print(f"Failed to retrieve user information for USER_ID: {user_id}")
        return

    name = user_response.json().get('username')

    print(f"User ID: {user_id}, Username: {name} OK")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py USER_ID")
    else:
        user_id = int(sys.argv[1])
        user_info(user_id)