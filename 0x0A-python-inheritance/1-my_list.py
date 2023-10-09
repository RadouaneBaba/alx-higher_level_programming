#!/usr/bin/python3

""" My list class"""


class MyList(list):
    """ class that prints ordered list """
    def print_sorted(self):
        print(sorted(self))
