#!/usr/bin/python3
"""model named 0-gather_data_from_an_API"""
import requests
from sys import argv


if __name__ == '__main__':

    id = argv[1]
    task = []
    done = 0
    total = 0
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    result = requests.get(url_user).json()
    name = result.get('name')
    todos = "https://jsonplaceholder.typicode.com/todos/"
    res_task = requests.get(todos).json()
    for i in res_task:
        if i.get('userId') == int(id):
            if i.get('completed') is True:
                task.append(i['title'])
                done += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, total))
    for x in task:
        print("\t {}".format(x))
