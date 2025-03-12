#!/usr/bin/python3
'''extend Python script to export data in the CSV format'''
from requests import get
from sys import argv


if __name__ == '__main__':
    em_id = int(argv[1])
    remp_res = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(em_id))
    remp_res = remp_res.json()
    response_tasks = get('https://jsonplaceholder.typicode.com/todos').json()

    USERNAME = remp_res['username']
    USER_ID = remp_res['id']
    FILE_NAME = '{}.csv'.format(em_id)

    with open(FILE_NAME, 'w', encoding='UTF-8') as csv_file:
        for task in response_tasks:
            if task['userId'] == em_id:
                TASK_COMPLETED_STATUS = task['completed']
                TASK_TITLE = task['title']
                record = '"{}","{}",\
"{}","{}"\n'.format(USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE)
                csv_file.write(record)
