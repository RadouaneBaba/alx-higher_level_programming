#!/usr/bin/python3

""" indentation module """


def text_indentation(text):
    """ text_indentation function """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        if c in ['.', '?', ':']:
            line += c
            print(line.strip())
            print("")
            line = ""
        else:
            line += c
    if line != "":
        print(line.strip())
