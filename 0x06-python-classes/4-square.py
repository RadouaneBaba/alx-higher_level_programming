#!/usr/bin/python3

"""
    define a square class
Classes:
    Square
"""


class Square:
    """ square class definition """
    def __init__(self, size=0):
        """
            initialise square object
        Args:
            size (int): size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        get square area
        Returns:
            area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        get size
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size
        Args:
            value (int): value for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
