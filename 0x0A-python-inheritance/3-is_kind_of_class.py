#!/usr/bin/python3
'''returns true if object is an instance of specified class
    or inherited from specified class'''


def is_kind_of_class(obj, a_class):
    '''returns true or false if class is inherited'''
    return isinstance(obj, a_class)
