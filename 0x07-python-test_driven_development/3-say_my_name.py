#!/usr/bin/python3

""" define a function that prints a sentence """


def say_my_name(first_name, last_name=""):
    """ print a sentence with args
    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
