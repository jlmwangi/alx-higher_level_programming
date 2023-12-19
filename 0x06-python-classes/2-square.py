#!/usr/bin/python3
"""define a square"""


class Square:
    def __init__(self, size=0):
        """ Initializes a square
        Args:
        - size (int): size of a square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
