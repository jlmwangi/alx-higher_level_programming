#!/usr/bin/python3
'''function that divides al elements of a matrix'''


def matrix_divided(matrix, div):
    '''divides matrix using div as the divisor and returns a new matrix'''

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    length = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if length is None:
            length = len(row)
        elif length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if type(n) is not int and type(n) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matr = [[round(n / div, 2) for n in row] for row in matrix]

    return matr
