#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gatherData():
    """Gather data from an API and export it to JSON"""
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            users = response.json()
            response = requests.get(todo_url)
            if response.status_code == 200:
                todos = response.json()
                with open('todo_all_employees.json', 'w') as jsonfile:
                    json.dump({user['id']: [{
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    } for todo in todos if todo['userId'] == user['id']]
                      for user in users}, jsonfile)
            else:
                print("An error occured")
        else:
            print("An error occured")
    except (Exception):
        print("An error occured")
        return 0


if __name__ == "__main__":
    """ Only executes as main"""
    gatherData()
