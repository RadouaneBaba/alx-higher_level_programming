#!/usr/bin/python3

""" module of read file func"""


def read_file(filename=""):
    """ func that reads a file """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f)
