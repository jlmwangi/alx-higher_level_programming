#!/usr/bin/python3
# takes a url, sends a request and displays value of variable X-Request-Id

import requests
import sys

if __name__ == "__main__":
    """runs as the main code"""
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
