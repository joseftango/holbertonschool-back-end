#!/usr/bin/python3
'''extend Python script to export data in the CSV format'''
from requests import get
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])
    remp_res = get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    remp_res = remp_res.json()
    response_tasks = get('https://jsonplaceholder.typicode.com/todos').json()

    USERNAME = remp_res['name']
    USER_ID = remp_res['id']
    FILE_NAME = f'{employee_id}.csv'

    with open(FILE_NAME, 'w', encoding='UTF-8') as csv_file:
        for task in response_tasks:
            if task['userId'] == employee_id:
                TASK_COMPLETED_STATUS = task['completed']
                TASK_TITLE = task['title']
                record = f'"{USER_ID}","{USERNAME}",\
"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\n'
                csv_file.write(record)
