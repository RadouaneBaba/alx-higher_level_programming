#!/usr/bin/python3

""" square class module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class subclass of rectangle """
    def __init__(self, size):
        super().__init__(size, size)
