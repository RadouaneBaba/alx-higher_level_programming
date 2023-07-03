#!/usr/bin/python3

""" define a function that prints square with the character # """


def print_square(size):
    """ print square with #
    Args:
        size (int): size of square
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
