#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for elem in my_list:
            print(elem, end="")
            n += 1
        print("")
    except ValueError:
        print("Error")
    finally:
        return n
