#!/usr/bin/python3

def roman_to_int(roman_string):
    
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0 
    if type(roman_string) != str or not roman_string:
        return 0

    for i in range(len(roman_string) - 1):
        c = roman_string[i]
        cn = roman_string[i + 1]
        if r_dict.get(c) >= r_dict.get(cn):
            result += r_dict.get(c)
        else:
            result -= r_dict.get(c)

    result += r_dict.get(roman_string[-1])
    return result
