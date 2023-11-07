#!/usr/bin/python3
""" module 2-recurse.py """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot
    articles for a given subreddit
    """

    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Test"}
    param = {"after": after}
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if response.status_code == 200:
        for i in range(len(response.json().get("data").get("children"))):
            hot_list.append(response.json().get("data")
                            .get("children")[i].get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
