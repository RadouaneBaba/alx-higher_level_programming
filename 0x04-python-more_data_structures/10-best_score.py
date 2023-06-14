#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for key in a_dictionary.keys():
        if a_dictionary.get(key) == max(a_dictionary.values()):
            return key
