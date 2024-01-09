#!/usr/bin/python3
'''function that returns a python data structure'''


import json


def from_json_string(my_str):
    '''returns an object represented by a JSON string'''
    from_json = json.loads(my_str)
    return from_json
