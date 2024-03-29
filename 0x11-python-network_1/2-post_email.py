#!/usr/bin/python3
# takes a url and an email, sends a post request to the url using the email
# displays body of the response(decoded in utf-8)

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":
    """runs as main code"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
        print(body)
