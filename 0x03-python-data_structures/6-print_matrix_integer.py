#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matrix_of_int in matrix:
        if len(matrix_of_int) == 0:
            print()
        for idx in range(len(matrix_of_int)):
            print("{:d}".format(matrix_of_int[idx]), end=" " if idx != len(matrix_of_int) - 1 else "\n")
