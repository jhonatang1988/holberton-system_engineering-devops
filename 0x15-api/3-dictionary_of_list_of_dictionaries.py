#!/usr/bin/python3
"""
fetch an employee task's progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    try:
        urlbase = "https://jsonplaceholder.typicode.com/"
        urltasks = "users/1/todos"
        urlusers = "users"

        rt = requests.get(urlbase + urltasks)
        ru = requests.get(urlbase + urlusers)

        tasks = rt.json()
        users = ru.json()

        usersdict = {}

        for user in users:
            id = user['id']
            username = user['username']
            taskslist = []
            for task in tasks:
                if task['userId'] == id:
                    taskslist.append({"task": task['title'],
                                      "completed": task['completed'],
                                      "username": username})
            usersdict[id] = taskslist

        filename = "todo_all_employees.json"

        with open(filename, 'w') as j:
            json.dump(usersdict, j)

    except ValueError:
        pass
