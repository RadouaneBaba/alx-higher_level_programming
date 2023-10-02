#!/usr/bin/python3

""" module of matrix divided function """

def matrix_divided(matrix, div):
    """ dividing a matrix by a num """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    new_mat = []
    for i in range(len(matrix)):
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for n in matrix[i]:
            new_row.append(round((n / div), 2))
        new_mat.append(new_row)
    return new_mat
