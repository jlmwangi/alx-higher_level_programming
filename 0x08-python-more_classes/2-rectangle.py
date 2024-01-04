#!/usr/bin/python3
''' Defines a rectangle based on 1-rectangle.py'''


class Rectangle:
    ''' represents a rectangle'''

    def __init__(self, width=0, height=0):
        """ initializes a rectangle with specified width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Getter method to retreive the width'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Getter method to retrieve the width'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets the rectangles height'''
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' gets the area of the rectangle'''
        return (self.width * self.height)

    def perimeter(self):
        ''' gets perimeter of rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)
