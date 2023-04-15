#!/usr/bin/python3
"""model named 0-gather_data_from_an_API"""
import json
import requests
import sys


def export_data_to_json():
    """function that extract data to export it in json"""
    USER_ID = sys.argv[1]
    data_user = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{USER_ID}').json()

    data_todos = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{USER_ID}/todos/').json()

    USERNAME = data_user['username']

    data_dict = {}
    data_dict[f'{USER_ID}'] = []
    for i in data_todos:
        todos_dict = {}
        todos_dict['task'] = i['title']
        todos_dict['completed'] = i['completed']
        todos_dict['username'] = USERNAME
        data_dict[f'{USER_ID}'].append(todos_dict)

    with open(f'{USER_ID}.json', 'w') as f:
        json.dump(data_dict, f)


if __name__ == '__main__':
    export_data_to_json()
