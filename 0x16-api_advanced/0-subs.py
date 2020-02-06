#!/usr/bin/python3
"""
return number of subscribers of subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'User-Agent: learningapi:v1.0.0 (by /u/jhonatang1988)'
    }

    rr = requests.get(url, headers=headers)

    about = rr.json()

    if 'data' in about:
        return about['data']['subscribers']
    else:
        return 0
