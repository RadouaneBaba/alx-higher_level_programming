#!/usr/bin/python3

""" inherits from mod """


def inheris_from(obj, a_class):
    """ check if object inherited from class """
    return issubclass(type(obj), a_class)
