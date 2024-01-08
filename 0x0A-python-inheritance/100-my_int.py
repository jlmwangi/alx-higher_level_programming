#!/usr/bin/python3
'''defines a class int'''


class MyInt(int):
    '''subclass MyInt derived from class int'''
    def __eq__(self, other):
        '''override the equality operator'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''override the inequality operator'''
        return super().__eq__(other)
