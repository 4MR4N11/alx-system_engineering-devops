#!/usr/bin/python3
""" module 0-subs.py """
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Test"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
