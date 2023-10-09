#!/usr/bin/python3

""" square class module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class subclass of rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f'[Square] {self.__width}/{self.__height}'
