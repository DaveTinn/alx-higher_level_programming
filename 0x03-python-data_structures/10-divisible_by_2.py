#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    div_by_2 = []
    for idx in my_list:
        if idx % 2 == 0:
            div_by_2.append(True)
        else:
            div_by_2.append(False)
    return div_by_2
