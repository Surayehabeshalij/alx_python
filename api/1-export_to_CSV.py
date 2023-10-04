#!/usr/bin/python3
'''
A script to export data in the CSV format.
'''

import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide the employee ID as a parameter.")
        sys.exit(1)
        
    uid = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()
        
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo = todo_response.json()
        
        with open(f"{uid}.csv", 'w', newline='') as csvfile:
            taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for t in todo:
                taskwriter.writerow([int(uid), user.get('username'),
                                     t.get('completed'),
                                     t.get('title')])
        print(f"Data exported to {uid}.csv")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")