#!/usr/bin/python3
"""define a square class"""


class Square:
    """Represents a square

    Attributes:
    - size (int): Represents size of each side"""

    def __init__(self, size):
        """
        initializes a square object

        Args:
        - size (int): size of each side of the square"""
        self.__size = size
