#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her 'TODO' list progress.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])
    remp_res = get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    remp_res = remp_res.json()
    response_tasks = get('https://jsonplaceholder.typicode.com/todos').json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    EMPLOYEE_NAME = remp_res['name']
    first_line = f'Employee {EMPLOYEE_NAME} is done with tasks'
    completed_taskes_title = []

    for task in response_tasks:
        if task['userId'] == employee_id:
            if task['completed']:
                NUMBER_OF_DONE_TASKS += 1
                completed_taskes_title.append(task['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    text = first_line + f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'

    for t in completed_taskes_title:
        text += '\n\t ' + t

    print(f'{text}')
