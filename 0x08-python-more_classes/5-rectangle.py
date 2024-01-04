#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """gets rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * self.height) * 2)

    def __str__(self):
        """string representation of rectangle"""
        rectangle_str = ""
        if self.width != 0 and self.height != 0:
            rectangle_str += "\n".join("#" * self.width
                                       for _ in range(self.height))
        return rectangle_str

    def __repr__(self):
        """string representation of a rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """delete rectangle"""
        print("Bye rectangle...")
