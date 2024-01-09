#!/usr/bin/python3
'''defines a function that reads a textfile'''


def read_file(filename=""):
    '''function that reads a UTF-8 textfile'''
    with open(filename, encoding='utf-8') as t:
        readfile = t.read()
        print(readfile)
