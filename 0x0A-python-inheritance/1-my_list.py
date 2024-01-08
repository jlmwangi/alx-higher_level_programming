#!/usr/bin/python3
'''defines a class'''


class MyList(list):
    '''defines a subclass MyList inherited from List'''
    def print_sorted(self):
        '''sort and print the list'''
        print(sorted(self))
