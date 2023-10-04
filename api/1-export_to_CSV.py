#!/usr/bin/python3
"""For a given employee ID, exports tasks owned by the employee to a CSV file"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    name = user.json().get('name')

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