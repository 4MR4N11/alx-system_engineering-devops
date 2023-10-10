#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the top 10
hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Test'}
    response = requests.get(url, headers=headers).json()
    try:
        for i in range(10):
            print(response['data']['children'][i]['data']['title'])
    except Exception:
        print(None)
