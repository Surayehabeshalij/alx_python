#!/usr/bin/python3
""" 2-export_to_JSON

    Export data in the JSON format.
"""
import json
import requests
import sys


def main():
    """According to user_id, export information in json
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py USER_ID")
        return

    user_id = sys.argv[1]
    if not user_id.isdigit():
        print("Invalid USER_ID. Please provide a valid integer.")
        return

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve user information for USER_ID: {user_id}")
        return

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO list for USER_ID: {user_id}")
        return

    name = user_response.json().get('username')
    todos = todos_response.json()
    tasks = []

    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": name
        }
        tasks.append(task)

    info = {user_id: tasks}
    file_name = f"{user_id}.json"
    with open(file_name, 'w') as file:
        json.dump(info, file)

    print(f"Data exported to {file_name} successfully.")


if __name__ == "__main__":
    main()