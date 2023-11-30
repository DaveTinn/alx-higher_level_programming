#!/usr/bin/python3
def add_argmt(argv):
    num_of_elements = len(argv) - 1
    if num_of_elements == 0:
        print("{:d}".format(num_of_elements))
    else:
        index = 1
        result = 0
        while index <= num_of_elements:
            result += int(argv[index])
            index += 1
        print("{:d}".format(result))


if __name__ == "__main__":
    import sys
    add_argmt(sys.argv)
