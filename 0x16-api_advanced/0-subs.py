#!/usr/bin/python3
import requests
"""  function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit."""


def number_of_subscribers(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers')
        else:
            return 0
    else:
        return 0
