#!/usr/bin/python3

""" define a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """matrix_divided divide a matarix by a number
    Args:
        matrix (list): the matrix
        div (float): number for division
    Returns:
        new matrix divided by div
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    lenn = len(matrix[0])
    new = []
    for row in matrix:
        if len(row) != lenn:
            raise TypeError("Each row of the matrix must have the same size")
        li = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(err)
            li.append(round(elem / div, 2))
        new.append(li)

    return new
