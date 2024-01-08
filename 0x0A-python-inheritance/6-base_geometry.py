#!/usr/bin/python3
'''creates a class that raises an exception'''


class BaseGeometry():
    '''defines a new class BaseGeometry'''
    def area(self):
        raise Exception("area() is not implemented")
