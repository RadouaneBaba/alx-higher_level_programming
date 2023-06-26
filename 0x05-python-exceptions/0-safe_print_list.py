#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for n in range(x):
            print(my_list[n], end="")
        print("")
    except ValueError:
        print("Error")
