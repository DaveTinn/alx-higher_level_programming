#!/usr/bin/python3
"""
Python Interpreter.
"""


def find_peak(list_of_integers):
    """
    Defines the function to find the peak
    in a list of unsorted integers.
    """
    length = len(list_of_integers)
    if list_of_integers == []:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = length // 2
    list_idx = list_of_integers[mid]
    if list_idx > list_of_integers[mid - 1] and\
            list_idx > list_of_integers[mid + 1]:
        return list_idx
    elif list_idx < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1::])
