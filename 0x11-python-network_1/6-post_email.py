#!/usr/bin/python3
""" takes a url and email,sends a post with email as parameter and displays body"""

import requests
import sys

if __name__ == "__main__":
    """python script to display body"""
    mail = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=mail)
    print(res.text)
