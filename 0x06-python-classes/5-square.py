#!/usr/bin/python3
""" define a square"""


class Square:
    def __init__(self, size=0):
        """ Initialize a square
        Args:
        - size (int): size of each side"""
        self.__size = size

    @property
    def size(self):
        """ Retrieve size of square
        Returns:
        - int: size of each side"""
        return self.__side

    @size.setter
    def size(self, value):
        """ Sets square size
        Args:
        - value (int): size of each side"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates area
        Returns:
        - int: area of square"""
        return self.__size * self.__size

    def my_print(self):
        """ print square using hashtags"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
