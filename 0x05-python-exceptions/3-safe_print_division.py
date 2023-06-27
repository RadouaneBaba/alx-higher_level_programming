#!/usr/bin/python3

def safe_print_division(a, b):
    n = None
    try:
        n = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(n))
        return n
