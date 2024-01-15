#!/usr/bin/python3
'''defines a class that inherits from rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''defines class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes class square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''gets size of square'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets square size'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def display(self):
        '''uses the character # to display itself'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print('', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''returns string representation of a square'''
        return f"[Square] ({self.id}) {self.x} / {self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''assigns attributes to the square class'''
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''returns dictionary representation of a square'''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
