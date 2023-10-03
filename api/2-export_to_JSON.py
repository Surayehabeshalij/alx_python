#!/usr/bin/python3
'''
A script to export data in the JSON format.
'''

import urllib.request
import json

def get_employee_details(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.loads(response.read().decode())
    employee_name = employee_data['name']

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    with urllib.request.urlopen(todo_url) as response:
        todos = json.loads(response.read().decode())

    # Calculate TODO list progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

    # Export data to JSON file
    file_name = f"{employee_id}.json"
    data = {
        employee_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_data['username']
            } for todo in todos
        ]
    }
    with open(file_name, 'w') as file:
        json.dump(data, file)


# Prompt user for employee ID
employee_id = int(input("Enter the employee ID: "))

# Call the function to get employee TODO list progress and export data to JSON file
get_employee_details(employee_id)