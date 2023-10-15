#!/usr/bin/python3

""" module for rectangle """
from base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        return y

    @y.setter
    def y(self, y):
        self.integer_validator("y", y)
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for a in range(self.__y):
            print("")
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        s = f"[Rectangle] ({self.id}) self.__x/self.__y"
        return f"{s} - self.__width/self.__height"
