#!/usr/bin/python3
'''function that appends a string at end of text file'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file'''
    with open(filename, 'a', encoding='utf-8') as a_write:
        chars_append = a_write.write(text)
    return chars_append
