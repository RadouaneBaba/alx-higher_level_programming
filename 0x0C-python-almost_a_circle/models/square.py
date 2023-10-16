#!/usr/bin/python3

""" square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string output """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if len(args) > 0:
            self.id = args[0] if len(args) >= 1 else self.id
            size = args[1] if len(args) >= 2 else self.size
            x = args[2] if len(args) >= 3 else self.x
            y = args[3] if len(args) >= 4 else self.y
        else:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            size = kwargs["size"] if "size" in kwargs else self.size
            x = kwargs["x"] if "x" in kwargs else self.x
            y = kwargs["y"] if "y" in kwargs else self.y

        self.integer_validator("width", size)
        self.integer_validator("x", x)
        self.integer_validator("y", y)

        self.size = size
        self.x = x
        self.y = y
