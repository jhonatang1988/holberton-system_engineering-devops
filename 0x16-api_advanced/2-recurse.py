#!/usr/bin/python3
"""
recursive way to get all results in paginated api
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    recurse
    """
    try:
        results = resultsperpage(subreddit, hot_list, after)
        if not results[0] and not results[1]:
            return None
        if results[0]:
            hot_list.append(results[0])
        if results[1]:
            after = results[1]
            recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return hot_list
    except Exception as e:
        print(e)


def resultsperpage(subreddit, hot_list=[], after=''):
    """
    resulsperpage
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json?raw_json=1&after={}"\
            .format(subreddit, after)

        headers = {
            'User-Agent': 'User-Agent: learningapi:v1.0.0 \
            (by /u/jhonatang1988)'
        }

        rr = requests.get(url, headers=headers, allow_redirects=False)

        if rr.status_code != 200:
            return [None, None]

        listing = rr.json()

        if 'data' in listing:
            posts = listing['data']['children']
            titlelist = list((map(gettitle, posts)))
            hot_list += titlelist
            return [hot_list, rmnonascii(listing['data']['after'])]
        else:
            return [hot_list, None]
    except Exception as e:
        print(e)


def gettitle(post):
    """
    get title from dict
    """
    return rmnonascii(post['data']['title'])


def rmnonascii(s):
    """
    rmnonascii
    """
    try:
        if s:
            return ''.join([c if 32 < ord(c) < 127 else " " for c in s])
        else:
            return s
    except:
        print('se jodio ascii')
