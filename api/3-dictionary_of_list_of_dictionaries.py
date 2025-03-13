#!/usr/bin/python3
'''
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
export data to the JSON format.
'''
import json
import requests
import sys


if __name__ == '__main__':
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(url_user).json()
    data = {}
    values = []

    for user in res:
        id = str(user['id'])
        username = user['username']
        res_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/' +
                id + '/todos').json()
        for t in res_tasks:
            values.append({'username': username, 'task': t['title'],
                           'completed': t['completed']})
        data[id] = values

    with open('todo_all_employees.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f)
