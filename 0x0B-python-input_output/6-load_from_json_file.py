#!/usr/bin/python3

""" module of load from json func """
import json


def load_from_json_file(filename):
    """ load objet from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
