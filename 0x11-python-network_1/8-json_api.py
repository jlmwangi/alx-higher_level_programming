#!/usr/bin/python3
# takes in a letter, sends a post request with the letter as parameter

import sys
import requests

if __name__ == "__main__":
    """takes in a letter as parameter"""
    try:
        q = sys.argv[1]
    except:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    load = {'q': q}
    req = requests.post(url, data=load)

    try:
        j_son = req.json()
        if len(j_son) == 0:
            print('No result')
        else:
            j_id = j_son.get('id')
            j_name = j_son.get('name')
            print(f"[{j_id}] {j_name}")
    except:
        print("Not a valid JSON")
