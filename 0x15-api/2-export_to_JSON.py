#!/usr/bin/python3
"""
fetch an employee task's progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and isinstance(sys.argv[1], str):
        try:
            employeeid = sys.argv[1]
            int(sys.argv[1])
            urlbase = "https://jsonplaceholder.typicode.com/"

            urltasks = "users/{}/todos".format(employeeid)

            urlprofile = "users/{}".format(employeeid)

            rt = requests.get(urlbase + urltasks)
            rp = requests.get(urlbase + urlprofile)

            tasks = rt.json()
            profile = rp.json()

            username = profile['username']

            taskslist = []

            for task in tasks:
                if task['userId'] == int(sys.argv[1]):
                    taskslist.append({"task": task['title'],
                                      "completed": task['completed'],
                                      "username": username})

            iddict = {sys.argv[1]: taskslist}
            filename = "{}.json".format(sys.argv[1])

            with open(filename, 'w') as j:
                json.dump(iddict, j)

        except ValueError:
            pass
    else:
        pass
