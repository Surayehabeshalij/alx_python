#!/usr/bin/python3
""" 1-export_to_CSV

    Export data in the CSV format.
"""
import csv
import requests
import sys


def main():
    """According to user_id, export information in CSV
    """
    user_id = sys.argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()

    with open(f"{user_id}.csv", 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'Username', 'Completed', 'Title'])
        for todo in request_todo:
            writer.writerow([user_id, name, todo.get('completed'), todo.get('title')])

    num_tasks = len(request_todo)
    print(f"Number of tasks in CSV: {num_tasks} OK")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()