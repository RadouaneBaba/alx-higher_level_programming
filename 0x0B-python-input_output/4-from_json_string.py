#!/usr/bin/python3

""" module for from_json_string func """
import json


def from_json_string(my_str):
    """ returns an object from json str"""
    return json.loads(my_str)
