#!/usr/bin/python3

""" write to a file and return nuber of chars """


def write_file(filename="", text=""):
    """ write to a file """
    with open(filename, 'a', encoding="utf-8") as f:
        n = 0
        for i in text:
            f.write(i)
            n += 1
        return n
