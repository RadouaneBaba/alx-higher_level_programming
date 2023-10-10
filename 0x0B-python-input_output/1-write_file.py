#!/usr/bin/python3

""" module of write file func """


def write_file(filename="", text=""):
    """ write text to a file """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
