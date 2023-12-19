#!/usr/bin/python3
'''Python Interpreter.'''


class Square:
    '''Defines a Square.'''

    def __init__(self, size=0):
        '''Instantiating an instance of the class.

        Arguments:
            size: size of the instance attribute.

        Raise:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Defines area of square.

        Returns:
            The current square area.
        '''
        return self.__size ** 2
