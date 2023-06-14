#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    result = 0

    for n in my_set:
        result = result + n

    return result
