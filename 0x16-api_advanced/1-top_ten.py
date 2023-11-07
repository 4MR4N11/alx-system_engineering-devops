#!/usr/bin/python3
""" module 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Test"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get("data").get("children")[i]
                  .get("data").get("title"))
    else:
        print(None)
