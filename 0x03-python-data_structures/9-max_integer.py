#!/usr/bin/python3
def max_integer(my_list=[]):
    n = 0
    if not my_list:
        return None
    for a in my_list:
        if n < a:
            n = a
    return n
