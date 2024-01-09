#!/usr/bin/python3
'''function that returns dictionary description'''


def class_to_json(obj):
    '''returns a dict with simple data structure(list, dictionary, etc)'''
    return obj.__dict__
