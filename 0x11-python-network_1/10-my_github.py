#!/usr/bin/python3
""" takes github credentials and uses github api to display id"""

import requests
import sys

if __name__ == "__main__":
    """display id"""
    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get('https://api.github.com/user',
                       auth=(username, password))

    user_data = res.json()
    print(user_data.get('id'))
