#!/usr/bin/python3
"""Script that exports data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [{"username": username, "task": task.get("title"),
                  "completed": task.get("completed")} for task in todos if task.get("userId") == user_id]
        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
