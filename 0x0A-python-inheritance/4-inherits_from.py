#!/usr/bin/python3
'''defines a function that checks whether an instance of
    a class is inherited'''


def inherits_from(obj, a_class):
    '''checks whether inheritance is direct or indirect'''
    return isinstance(obj, a_class)
