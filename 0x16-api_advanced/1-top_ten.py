#!/usr/bin/python3
"""
get 10 hot posts from subreddit
"""
import requests
import re


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        'User-Agent': 'User-Agent: learningapi:v1.0.0 (by /u/jhonatang1988)'
    }

    rr = requests.get(url, headers=headers, allow_redirects=False)

    listing = rr.json()

    if 'data' in listing:
        if 'children' in listing['data']:
            children = listing['data']['children']
            for child in children:
                for key, value in child['data'].items():
                    if key == 'title':
                        print(rmnonascii(value))
    else:
        print(None)

def rmnonascii(s):
    return ''.join([c if 32 < ord(c) < 127 else " " for c in s])
