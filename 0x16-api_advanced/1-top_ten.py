#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'soufiane'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(url, headers=user_agent, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])

        for item in data:
            title = item.get('data', {}).get('title', '')
            print(title)
    else:
        print("None")
