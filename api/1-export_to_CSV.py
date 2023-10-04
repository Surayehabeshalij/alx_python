#!/usr/bin/python3
"""For a given employee ID, exports tasks owned by the employee to a CSV file"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    if user.status_code != 200:
        print("Failed to retrieve user data. Please check the employee ID.")
        sys.exit(1)

    try:
        name = user.json().get('name')
        if not name:
            raise ValueError("Username not found.")
    except (KeyError, ValueError) as e:
        print("Failed to retrieve username:", str(e))
        sys.exit(1)

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasks = []
    for task in todos.json():
        if task.get('userId') == int(userId):
            taskId = task.get('id')
            completedStatus = str(task.get('completed'))
            title = task.get('title')
            tasks.append([userId, name, completedStatus, title])

    if tasks:
        filename = "{}.csv".format(userId)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(tasks)
        print("Data exported to {}".format(filename))
    else:
        print("No tasks found for the specified employee ID.")