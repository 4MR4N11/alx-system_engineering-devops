#!/usr/bin/python3
""" Function use recursion to get all titles of hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Function use recursion to get all titles of hot articles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Test'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
