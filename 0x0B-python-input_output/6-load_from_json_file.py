#!/usr/bin/python3
'''function that creates an object'''


import json


def load_from_json_file(filename):
    '''creates an object from a JSON file'''
    with open(filename, 'r', encoding='utf-8') as load_json:
        data_loaded = json.load(load_json)
    return data_loaded
