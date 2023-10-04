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

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        if len(todos) == 0:
            print("No tasks found for the specified employee ID.")
            sys.exit(1)

        filename = f"{employee_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos:
                task_completed_status = "Completed" if todo['completed'] else "Incomplete"
                writer.writerow([employee_id, user['username'], task_completed_status, todo['title']])

        print(f"Data exported to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")