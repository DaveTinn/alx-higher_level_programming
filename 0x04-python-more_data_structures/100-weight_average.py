#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        return sum(s * w for s, w in my_list) / sum(s for w, s in my_list)
