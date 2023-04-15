#!/usr/bin/python3
"""model named 0-gather_data_from_an_API"""
import json
import requests


def export_data_to_json():
    """function that extract data to export it in json"""
    data_users = requests.get(f'https://jsonplaceholder.\
typicode.com/users/').json()

    data_todos = requests.get(f'https://jsonplaceholder.\
typicode.com/todos/').json()
    data_dict = {}
    for obj in data_users:
        data_dict[f"{obj['id']}"] = []
        data_todos_user = requests.get(f"https://jsonplaceholder.\
typicode.com/user/{obj['id']}/todos/").json()
        for i in data_todos_user:
            todos_dict = {}
            todos_dict['username'] = obj['username']
            todos_dict['task'] = i['title']
            todos_dict['completed'] = i['completed']
            data_dict[f"{obj['id']}"].append(todos_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_dict, f)


if __name__ == '__main__':
    export_data_to_json()
