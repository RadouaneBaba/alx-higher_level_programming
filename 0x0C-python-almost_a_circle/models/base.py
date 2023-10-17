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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json of list """
        if list_dictionaries in [None, []]:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        f_name = f"{cls.__name__}.json"
        with open(f_name, 'w', encoding="utf-8") as f:
            llist = []
            if list_objs is None:
                f.write("[]")
            else:
                for e in list_objs:
                    llist.append(e.to_dictionary())
                f.write(Base.to_json_string(llist))

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        if json_string in [None, []]:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create instance """
        r0 = cls(10, 10, 10)
        r0.update(**dictionary)
        return r0

    @classmethod
    def load_from_file(cls):
        """ load from file """
        filename = f"{cls}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                llist = []
                json_list = Base.from_json_string(f.read())
                for j in json_list:
                    instance = cls.create(j)
                    llist.append(instance)
                return llist
        except FileNotFoundError:
            return []
