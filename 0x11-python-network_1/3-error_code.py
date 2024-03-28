#!/usr/bin/python3
# takes a url, sends a request and displays body of response decoded in utf-8

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    """runs to take a url if its run as main code"""
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error Code: ", e.status)
