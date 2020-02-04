#!/usr/bin/python3
"""
fetch an employee task's progress
"""
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

            NUMBER_OF_DONE_TASKS = 0
            TOTAL_NUMBER_OF_TASKS = 0
            tasktitlelist = []

            for task in tasks:
                if task['userId'] == int(employeeid):
                    if task['completed']:
                        NUMBER_OF_DONE_TASKS += 1
                        tasktitlelist.append(task['title'])
                    TOTAL_NUMBER_OF_TASKS += 1

            EMPLOYEE_NAME = profile['name']

            print("Employee {} is done with tasks({}/{}):"
                  .format(EMPLOYEE_NAME,
                          NUMBER_OF_DONE_TASKS,
                          TOTAL_NUMBER_OF_TASKS))

            for tasktitle in tasktitlelist:
                print("\t {}".format(tasktitle))
        except ValueError:
            pass
    else:
        pass
