#!/usr/bin/python3
"""function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit."""
import requests


def get_reddit_posts(subreddit, after=None):
    user_agent = {'User-Agent': 'soufiane'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    response = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after_data = data.get("after")
    children = data.get("children")

    post_titles = [post["data"]["title"] for post in children]

    if not after_data:
        return post_titles
    else:
        return post_titles + get_reddit_posts(subreddit, after=after_data)


def recurse(subreddit):
    return get_reddit_posts(subreddit)
