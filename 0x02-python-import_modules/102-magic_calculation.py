#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for index in range(1, 3):
            c = add(c, index)
        return (c)
    else:
        return sub(a, b)
