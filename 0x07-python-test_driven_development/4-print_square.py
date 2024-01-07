#!/usr/bin/python3
'''defines a function that prints a square'''


def print_square(size):
    '''this function prints a square with the character #'''
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
