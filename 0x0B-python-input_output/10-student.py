#!/usr/bin/python3
'''defines a student class'''


class Student:
    '''class defining a student'''
    def __init__(self, first_name, last_name, age):
        '''initializes class student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves dictionary representation of a student instance'''
        dict_json = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if hasattr(self, attr):
                dict_json[attr] = getattr(self, attr)
        return dict_json
