#!/usr/bin/python3

""" print square module """

def print_square(size):
    """ print square of size size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i < size - 1:
            print("")
