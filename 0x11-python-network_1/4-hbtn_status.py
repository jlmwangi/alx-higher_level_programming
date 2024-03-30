#!/usr/bin/python3
""" uses request package to fetch "https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    """runs only as main code"""
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
