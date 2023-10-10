#!/usr/bin/python3

""" module of student class """


class Student:
    """ define student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for attr in attrs:
                if type(attr) != str:
                    return self.__dict__
            f_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    f_dict[attr] = self.__dict__[attr]
            return f_dict
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
