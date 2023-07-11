#!/usr/bin/python3

""" append to a file """


def append_write(filename="", text=""):
    """ function """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
