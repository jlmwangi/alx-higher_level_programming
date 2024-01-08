#!/usr/bin/python3
'''function that adds a new attribute to an object'''


class person:

    def __init__(self):
        pass

    def add_attribute(self, att_name):
        if not hasattr(self, att_name):
            setattr(self, att_name)
        else:
            raise TypeError("can't add new attribute")
