#!/usr/bin/python3
'''defines a function that returns true if obj is
    an instance of specified class'''


def is_same_class(obj, a_class):
    '''checks if object is instance of specifies class'''
    return type(obj) == a_class
