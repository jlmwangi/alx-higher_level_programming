#!/usr/bin/python3
'''defines a class base geometry that validates integers'''


class BaseGeometry():
    '''create a class named BaseGeometry'''

    def area(self):
        '''calculates area of self'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function that checks whether value is an int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
