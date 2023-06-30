#!/usr/bin/python3

"""
    define a square class
Classes:
    Square
"""


class Square:
    """ square class definition """
    def __init__(self, size=0, position=(0, 0)):
        """
            initialise square object
        Args:
            size (int): size of square
            position (tuple): position
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0 or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__postion = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1]) != int or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__postion = value

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
