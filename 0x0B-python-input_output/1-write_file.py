#!/usr/bin/python3
'''function writes a string to a text file'''


def write_file(filename="", text=""):
    '''writes a string to a utf-8 text file'''
    with open(filename, 'w', encoding='utf-8') as wfile:
        chars_wrote = wfile.write(text)
    return chars_wrote
