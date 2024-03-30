#!/usr/bin/python3
"""takes a url, sends a request and displays body of response"""

import sys
import requests

if __name__ == "__main__":
    """script to display error code"""
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
