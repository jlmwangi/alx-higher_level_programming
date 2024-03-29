#!/usr/bin/python3
# takes in a url, sends a request and displays value of X-Request-Id

import sys
from urllib.request import urlopen


if __name__ == "__main__":
    """runs only if its main code"""
    url = sys.argv[1]

    with urlopen(url) as res:
        print(res.headers.get('X-Request-Id'))
