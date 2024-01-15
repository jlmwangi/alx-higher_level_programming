#!/usr/bin/python3
'''defines a class Rectangle that inherits from Base'''


import json
from models.base import Base


class Rectangle(Base):
    '''class Rectangle inheriting from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes the rectangle with width, height, x and y'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''gets the width of the rectangle'''
        return self.__width

    @property
    def height(self):
        '''gets the height of rectangle'''
        return self.__height

    @property
    def x(self):
        '''gets the value x of the rectangle'''
        return self.__x

    @property
    def y(self):
        '''gets the value y of the rectangle'''
        return self.__y

    @width.setter
    def width(self, width):
        '''sets the width of rectangle'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        '''sets the height of the rectangle'''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        '''sets the value x of the rectangle'''
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        '''sets the value y of the rectangle'''
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''finds area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''uses the character # to display itself'''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print('', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        '''returns a string rep of the rectangle'''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
                - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''returns dictionary representation of rectangle'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
