#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_value = 0
    max_key_value = None
    for key, value in a_dictionary.items():
        if value > key_value:
            key_value = value
            max_key_value = key
    return max_key_value
