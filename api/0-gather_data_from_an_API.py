from sys import argv
from requests import get

employee_id = int(argv[1])
response_employee_info = get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
response_tasks = get('https://jsonplaceholder.typicode.com/todos').json()

NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
EMPLOYEE_NAME = response_employee_info['name']
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

print(text)
