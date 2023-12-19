#!/usr/bin/python3
"""defines a square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
        - size (int): size of each side
        - position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position square"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(n, int) for n in value) \
                or not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print square using '#'"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
