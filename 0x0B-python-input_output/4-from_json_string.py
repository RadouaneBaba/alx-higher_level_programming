#!/usr/bin/python3

import json

""" module for from_json_string func """


def from_json_string(my_str):
    """ returns an object from json str"""
    return json.loads(my_str)
