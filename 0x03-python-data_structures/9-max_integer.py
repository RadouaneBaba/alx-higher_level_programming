#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    n = my_list[0]
    for a in my_list:
        if n < a:
            n = a
    return n
