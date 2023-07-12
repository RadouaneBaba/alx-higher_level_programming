#!/usr/bin/python3
""" module """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        my_obj = {}
        for s in attrs:
            if s in self.__dict__:
                my_obj[s] = self.__dict__[s]
        return my_obj
