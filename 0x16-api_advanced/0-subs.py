#!/usr/bin/python3
"""function that queries the Reddit API and returns number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Test'}
    response = requests.get(url, headers=headers).json()
    try:
        return response['data']['subscribers']
    except Exception:
        return 0
