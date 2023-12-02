#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_of_int in matrix:
        for print_matrix in matrix_of_int:
            print("{:d}".format(print_matrix), end=" ")
        print()
