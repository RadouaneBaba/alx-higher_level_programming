#!/usr/bin/python3

""" module class to json func """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure """
    return obj.__dict__
