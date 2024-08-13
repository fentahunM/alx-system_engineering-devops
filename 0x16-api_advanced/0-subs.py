#!/usr/bin/python3
""" returns the number of subscribers """

import requests as req


def number_of_subscribers(subreddit):
    """ this will return the number of subs of a given subreddit """

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Python script)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = req.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return 0
