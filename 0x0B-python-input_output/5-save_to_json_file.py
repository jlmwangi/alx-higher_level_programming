#!/usr/bin/python3
'''function that writes an object to a text file'''


import json


def save_to_json_file(my_obj, filename):
    '''writes an object to a file using json representation'''
    with open(filename, 'w', encoding='utf-8') as file_json:
        json.dump(my_obj, file_json)
