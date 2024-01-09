#!/usr/bin/python3
'''function that returns JSON representation of an object'''


import json

def to_json_string(my_obj):
    '''returns JSON representation of an object'''
    j_str = json.dumps(my_obj)
    return j_str
