#!/usr/bin/python3
"""Python Interpreter."""


def matrix_divided(matrix, div):
    """Retrieves the division of a elements of a matrix.

    Arguments:
        matrix: Matrix containing the elements to be divided
        div: The division.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
                    or If each row of the matrix is not the same size
                    or div is not a number
        ZeroDivisionERror: If div is equal to 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for idx in row:
            if not isinstance(idx, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    return [[round(idx / div, 2) for idx in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
