#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_response.json()

    todo_response = requests.get(url + "todos", params={"userId": employee_id})
    todo_data = todo_response.json()

    completed_tasks = [task for task in todo_data if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(todo_data)))

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
