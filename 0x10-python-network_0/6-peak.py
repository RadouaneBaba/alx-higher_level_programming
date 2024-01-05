#!/usr/bin/python3
""" find a peak in list """


def find_peak(list_of_integers):
    """ func to find peak """
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for n in list_of_integers:
        if n < peak:
            return peak
        if n > peak:
            peak = n
    return peak
