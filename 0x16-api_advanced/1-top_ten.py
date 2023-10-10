#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the top 10
hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Test'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        for child in children[:10]:
            print(child.get('data').get('title'))
    else:
        print(None)
