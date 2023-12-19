#!/usr/bin/python3
""" define a square class """


class Square:
    def __init__(self, size=0):
        """ Initializes a square
        Args:
        - size (int): size of each side of the square"""
        self.__size = size

    @property
    def size(self):
        """ Retrieve size of square
        Returns:
        - int: size of each side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets square size
        Args:
        - value (int): size of each side """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate area of a square
        Returns:
        - int: area of a square"""

        return self.__size * self.__size
