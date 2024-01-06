#!/usr/bin/python3
""" find a peak in list """


def find_peak(list_of_integers):
    """ func to find peak """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2

    parent = list_of_integers[mid]

    if mid - 1 >= 0:
        left = list_of_integers[mid - 1]
    else:
        left = mid
    if mid + 1 < len(list_of_integers):
        right = list_of_integers[mid + 1]
    else:
        right = mid

    if parent > left and parent > right:
        return parent
    elif left >= parent:
        return find_peak(list_of_integers[:mid])
    elif right >= parent:
        return find_peak(list_of_integers[mid + 1:])
