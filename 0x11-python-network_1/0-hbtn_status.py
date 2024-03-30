#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import urllib.request


def hbtn_status():
    """fetches https://alx-intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        html = r.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))


if __name__ == "__main__":
    hbtn_status()
