#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """gets perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        """string rep of a rectangle"""
        rectangle_str = ""
        if self.width != 0 and self.height != 0:
            rectangle_str += "\n".join(str(self.print_symbol) * self.width
                                       for _ in range(self.height))
        return rectangle_str

    def __repr__(self):
        """string representation of a rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a1 = rect_1.width * rect_1.height
        a2 = rect_2.width * rect_2.height

        if a1 >= a2:
            return rect_1
        else:
            return rect_2
