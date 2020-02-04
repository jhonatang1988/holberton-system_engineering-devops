#!/usr/bin/python3
"""
fetch an employee task's progress
"""
import requests
import sys
import csv

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

            name = profile['name']

            f = csv.writer(open("2.csv",
                                "w",
                                newline=''), quoting=csv.QUOTE_ALL)

            for task in tasks:
                if task['userId'] == int(employeeid):
                    f.writerow([task['userId'],
                                name,
                                task['completed'],
                                task['title']])

        except ValueError:
            pass
    else:
        pass
