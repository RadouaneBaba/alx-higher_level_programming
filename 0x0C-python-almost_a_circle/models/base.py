#!/usr/bin/python3

""" module of base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ construcotr func """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ json of list """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
