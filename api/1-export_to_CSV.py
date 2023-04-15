#!/usr/bin/python3
"""model named 0-gather_data_from_an_API"""
import requests
from sys import argv
import csv


def export_data_to_csv():
    """function that print extracted data"""
    USER_ID = argv[1]
    data_user = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{USER_ID}').json()

    data_todos = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{USER_ID}/todos/').json()

    USERNAME = data_user['username']

    with open('USER_ID.csv', 'w') as f:
        writer = csv.writer(f)
        for i in data_todos:
            writer.writerow([f"{i['userId']}", f"{USERNAME}",
                            f"{i['completed']}", f"{i['title']}"])


if __name__ == '__main__':
    export_data_to_csv()
