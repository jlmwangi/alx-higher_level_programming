#!/usr/bin/python3
'''script that adds all arguments to a python list'''


import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_new = []
if path.isfile("add_item.json"):
        list_existing = load_from_json_file('add_item.json')
save_to_json_file(list_new + sys.argv[1:], 'add_item.json')
