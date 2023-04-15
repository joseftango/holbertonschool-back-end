#!/usr/bin/python3
"""model named 0-gather_data_from_an_API"""
import requests
from sys import argv


def extract_data():
    """function that print extracted data"""
    empolyee_id = argv[1]
    data_user = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{empolyee_id}').json()

    data_todos = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{empolyee_id}/todos/').json()

    EMPLOYEE_NAME = data_user['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    str2 = ""
    for item in range(len(data_todos)):
        if data_todos[item]['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
            if item == len(data_todos) - 1:
                str2 += f"\t {data_todos[item]['title']}"
            else:
                str2 += f"\t {data_todos[item]['title']}\n"
        TOTAL_NUMBER_OF_TASKS += 1

    str1 = f"Employee {EMPLOYEE_NAME} is done with\
tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    final = str1 + '\n' + str2
    print(final)


if __name__ == '__main__':
    extract_data()
