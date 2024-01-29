import json
import requests


def get_all_todos():
    url_users = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url_users).json()

    all_todos = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        todos = requests.get(url_todos).json()

        user_todos = []
        for todo in todos:
            user_todos.append({
                'username': username,
                'task': todo['title'],
                'completed': todo['completed']
            })

        all_todos[user_id] = user_todos

    return all_todos


if __name__ == '__main__':
    all_todos = get_all_todos()

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_todos, json_file, indent=4)

    print("Data exported successfully to todo_all_employees.json")

