#!/usr/bin/python3
"""Python Interpreter"""


def pascal_triangle(n):
    if n <= 0:
        return []
    p_triangle = []

    while len(p_triangle) != n:
        for idx in range(n):
            row = [1] * (idx + 1)

            for i in range(1, idx):
                row[i] = p_triangle[idx - 1][i - 1] + p_triangle[idx - 1][i]
            p_triangle.append(row)

    return p_triangle
