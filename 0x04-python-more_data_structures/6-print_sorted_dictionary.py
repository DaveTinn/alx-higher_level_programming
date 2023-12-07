#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys_in_order in sorted(a_dictionary.keys()):
        print("{}: {}".format(keys_in_order, a_dictionary[keys_in_order]))
