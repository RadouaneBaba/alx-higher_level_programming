#!/usr/bin/python3

""" module of append_write func """


def append_write(filename="", text=""):
    """ append text to the end of a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
