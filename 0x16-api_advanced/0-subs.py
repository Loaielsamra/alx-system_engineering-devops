#!/usr/bin/python3
"""Queries the reddit api and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers in `subreddit`"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0

    result = response.json().get("data")
    return result.get("subscribers")
