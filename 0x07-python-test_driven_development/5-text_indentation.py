#!/usr/bin/python3

""" define a function that transforms a string """


def text_indentation(text):
    """ indent text
    Args:
        text (str): string to transform and print
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        if c in ['.', '?', ':']:
            line += c
            print(line.strip(), end="\n\n")
            line = ""
        else:
            line += c
    if (line != ""):
        print(line.strip())
