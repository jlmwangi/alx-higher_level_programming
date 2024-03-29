#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import urllib.request


def hbtn_status():
    """fetches https://alx-intranet.hbtn.io/status"""
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as r:
        html = r.read()
        print("Body response:")
        print("    - type:", type(html))
        print("    - content:", html)
        print("    - utf8 content:", html.decode('utf-8'))


if __name__ == "__main__":
    hbtn_status()
