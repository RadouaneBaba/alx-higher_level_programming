#!/usr/bin/python3

"""define a function that adds two integers"""


def add_integer(a, b=98):
    """add two integers
    Args:
        a (int): first num
        b (int): second num
    Returns:
        (int): sum of two nums
    Raises:
        TypeError: one of parameters is not an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
