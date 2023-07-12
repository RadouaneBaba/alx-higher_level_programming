#!/usr/bin/python3

""" module """


def pascal_triangle(n):
    """ function """
    if n <= 0:
        return []
    prev = []
    for i in range(n):
        for j in range(i + 1):
            if len(prev) == 0:
                s = 1
            elif (j - 1) < 0:
                s = prev[j]
            elif j == len(prev):
                s = prev[j - 1]
            else:
                s = prev[j - 1] + prev[j]
            my_list.append(s)
        print(my_list)
        prev = my_list
