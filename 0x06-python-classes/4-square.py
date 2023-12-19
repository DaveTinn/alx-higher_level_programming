#!/usr/bin/python3
'''Python Interpreter.'''


class Square:
    '''Defines a class Square.'''

    def __init__(self, size=0):
        '''Instantiating an instance of the class.

        arguments:
            size: size of the instance attribute.
        '''
        self.size = size

    @property
    def size(self):
        '''Property to retrieve instance attribute.

        Raise:
            TypeError: must be an integer else raise TypeError
            ValueError: if size is less than 0
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property to set instance attribute'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Defines area of square.

        Returns:
            The current square area.
        '''
        return self.__size ** 2
