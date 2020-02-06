#!/usr/bin/python3
"""
get 10 hot posts from subreddit
"""
import requests


def top_ten(subreddit):
    """
    top_ten
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        'User-Agent': 'User-Agent: learningapi:v1.0.0 (by /u/jhonatang1988)'
    }

    payload = {
        'limit': 10
    }

    rr = requests.get(url,
                      headers=headers,
                      params=payload,
                      allow_redirects=False)

    if rr.status_code != 200:
        print(None)
        return None

    listing = rr.json()

    if 'data' in listing:
        if 'children' in listing['data']:
            children = listing['data']['children']
            for child in children:
                for key, value in child['data'].items():
                    if key == 'title':
                        print(rmnonascii(value))


def rmnonascii(s):
    """
    remove non ascii
    """
    return ''.join([c if 32 < ord(c) < 127 else " " for c in s])
