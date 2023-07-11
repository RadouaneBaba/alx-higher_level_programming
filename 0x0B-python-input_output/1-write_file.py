#!/usr/bin/python3

""" write to a file and return nuber of chars """


def write_file(filename="", text=""):
    """ write to a file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
