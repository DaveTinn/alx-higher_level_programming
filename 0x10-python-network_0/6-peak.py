#!/usr/bin/python3



def find_peak(list_of_integers):
    peak = len(list_of_integers)
    if peak == 1:
        return list_of_intgers[0]
    elif peak == 2:
        return max(list_of_integers)
