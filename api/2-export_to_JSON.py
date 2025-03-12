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
    id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id
    res = requests.get(url_user).json()
    u = res.get('username')
    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id) + '/todos').json()

    data = {f'{id}': []}
    for d in res:
        my_dic = {'task': d['title'],
                  'completed': d['completed'], 'username': u}
        data[f'{id}'].append(my_dic)

    with open(f'{2}.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f)
