#!/usr/bin/python3
"""Python Interpreter."""


def add_integer(a, b=98):
    """
    Retrieves the sum of two integers.

    Arguments:
        a (int): The first integer.
        b (int): The second integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
