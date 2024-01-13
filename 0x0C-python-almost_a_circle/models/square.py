#!/usr/bin/python3
"""
Python Interpreter

The class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Instantiating the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Defining the instances of the class Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Gets the size of the class Square"""
        return self.height

    @size.setter
    def size(self, value):
        """Sets the size of the class Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method assigning attributes to the class"""
        attrs = ['id', 'size', 'x', 'y']

        for idx in range(len(args)):
            setattr(self, attrs[idx], args[idx])

        for key, value in kwargs.items():
            setattr(self, key, value)
