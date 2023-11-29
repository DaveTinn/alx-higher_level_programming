#!/usr/bin/python3
def upper_string(alphabet):
    if ord(alphabet) >= 97 and ord(alphabet) <= 122:
        return (ord(alphabet) - 32)
    else:
        return ord(alphabet)


def uppercase(str):
    lower_string = ""
    for alphabet in str:
        lower_string += "%c" % upper_string(alphabet)
    print("{:s}".format(lower_string))
