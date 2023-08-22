#!/usr/bin/python3
"""Script thats gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    completed_tasks = []
    for task in todo:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo)))

    for task in completed_tasks:
        print("\t {}".format(task))
