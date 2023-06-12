#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = (tuple_a[0] or 0) + (tuple_b[0] or 0)
    b = (tuple_a[1] or 0) + (tuple_b[1] or 0)

    tup = (a, b)

    return tup
