import json
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
    username = user_data.get("username")

    todo_response = requests.get(url + "todos", params={"userId": employee_id})
    todo_data = todo_response.json()

    user_dict = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            for task in todo_data
        ]
    }

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(user_dict, jsonfile)
