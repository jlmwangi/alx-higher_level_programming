#!/usr/bin/python3
'''defines a class base geometry that validates input'''


class BaseGeometry():
    '''create a class named BaseGeometry'''

    def area(self, width, height):
        '''calculates area of self'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function that checks whether value is an int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''creates a class Rectangle'''

    def __init__(self, width, height):
        '''initializes a class rectangle with width and height'''
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        '''calculates area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''returns rectangle description'''
        return "[Rectangle] {} / {}".format(self.__width, self.__height)


class Square(Rectangle):
    '''creates a class square inherited from rectangle'''

    def __init__(self, size):
        '''initializes a square with size'''
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        '''returns area of square'''
        return self.__size * self.__size
