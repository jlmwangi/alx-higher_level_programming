#!/usr/bin/python3
"""define a class square"""


class Square:
    def __init__(self, size=0):
        """ Initializes a square with a specified size
        Args:
        - size (int) - represents size of each side"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ finds area of a square
        Returns:
        - int: Area of the square"""
        return self.__size * self.__size
