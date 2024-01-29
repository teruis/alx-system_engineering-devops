import json
import requests
import sys


def get_user_todo_list():
    employee_id = int(sys.argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    url2 = '%s/todos' % url1
    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()
    completed_todo = []

    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo.append({"task": todo.get('title'), "completed": True, "username": user.get('username')})

    user_todo_data = {str(employee_id): completed_todo}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(user_todo_data, json_file, indent=4)

    print("Data exported successfully to {}.json".format(employee_id))


if __name__ == '__main__':
    get_user_todo_list()

