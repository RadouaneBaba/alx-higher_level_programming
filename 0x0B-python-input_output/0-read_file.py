#!/usr/bin/python3

""" define a fnction that reads a text file and print it """


def read_file(filename=""):
    """ func """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
