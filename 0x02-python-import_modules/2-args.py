#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argmt = sys.argv
    num_of_elements = len(argmt) - 1
    if num_of_elements > 1:
        print("{} arguments:".format(num_of_elements))
        for index in range(1, num_of_elements + 1):
            print("{}: {}".format(num_of_elements, argmt[index]))
    elif num_of_elements == 0:
        print("{} arguments.".format(num_of_elements))
    else:
        print("{} arguments:".format(num_of_elements))
        print("{}: {}".format(num_of_elements, argmt[1]))
