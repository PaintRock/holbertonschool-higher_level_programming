#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):

    if div is None:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for i in range(len(row)):
            if not isinstance(row[i], int) and not isinstance(row[i], float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    return [[round(row[i] / div, 2) for i in range(len(row))]
            for row in matrix]
