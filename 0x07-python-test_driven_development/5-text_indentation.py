#!/usr/bin/python3
'''prints a text with 2 new lines after each of these; ., ?, :'''


def text_indentation(text):
    '''splits text into lines followed by 2 blank lines'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    mark = 0
    for c in text:
        if mark == 0:
            if c == ' ':
                continue
            else:
                mark = 1
        if mark == 1:
            if c == '.' or c == '?' or c == ':':
                print(c)
                print()
                mark = 0
            else:
                print(c, end="")
