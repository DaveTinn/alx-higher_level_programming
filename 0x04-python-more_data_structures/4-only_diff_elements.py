#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_of_elements = set(set_1 ^ set_2)
    return set_of_elements
