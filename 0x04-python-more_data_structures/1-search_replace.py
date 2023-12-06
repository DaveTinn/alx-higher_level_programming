#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda s_r: replace if s_r == search else s_r, my_list))
    return new_list
