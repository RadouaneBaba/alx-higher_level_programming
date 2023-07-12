#!/usr/bin/python3

""" module """


def pascal_triangle(n):
    """ function """
    if n <= 0:
        return []
    prev = []
    for i in range(n):
        my_list = []
        for j in range(i + 1):
            if len(prev) == 0:
                s = 1
            elif (j - 1) < 0:
                s = prev[-1][j]
            elif j == len(prev):
                s = prev[-1][j - 1]
            else:
                s = prev[-1][j - 1] + prev[-1][j]
            my_list.append(s)
        prev.append(my_list)
    return prev
