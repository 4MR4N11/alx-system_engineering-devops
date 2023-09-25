#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def gatherData(employeeID):
    """Gather data from an API and print it"""
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            user = response.json()
            response = requests.get(todo_url)
            if response.status_code == 200:
                todos = response.json()
                completed = []
                for todo in todos:
                    if todo['completed'] is True:
                        completed.append(todo)
                print("Employee {} is done with tasks({}/{}):"
                      .format(user['name'], len(completed), len(todos)))
                for todo in completed:
                    print("\t {}".format(todo['title']))
            else:
                print("An error occured")
        else:
            print("An error occured")
    except (Exception):
        print("An error occured")
        return 0


if __name__ == "__main__":
    """ Only executes as main"""
    if len(argv) == 2 and argv[1].isdigit():
        gatherData(argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
