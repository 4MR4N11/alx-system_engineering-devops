#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gatherData(employeeID):
    """gather data from an API and export it to JSON"""
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            user = response.json()
            response = requests.get(todo_url)
            if response.status_code == 200:
                todos = response.json()
                with open('{}.json'.format(employeeID), 'w') as jsonfile:
                    json.dump({employeeID: [{
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    } for todo in todos]}, jsonfile)
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
        print("Usage: ./2-export_to_JSON.py <employee ID>")
