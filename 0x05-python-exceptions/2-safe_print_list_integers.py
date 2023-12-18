#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    d, idx = 0, 0
    while d < x:
        try:
            print("{:d}".format(my_list[d]), end="")
            idx += 1
        except (ValueError, TypeError):
            pass
        d += 1
    print()
    return idx
