#!/usr/bin/python3

""" module for rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor doc """
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
        """ method doc """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """ method doc """
        return self.__width

    @width.setter
    def width(self, width):
        """ method doc """
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """ method doc """
        return self.__height

    @height.setter
    def height(self, height):
        """ method doc """
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """ method doc """
        return self.__x

    @x.setter
    def x(self, x):
        """ method doc """
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """ method doc """
        return y

    @y.setter
    def y(self, y):
        """ method doc """
        self.integer_validator("y", y)
        self.__y = y

    def area(self):
        """ method doc """
        return self.__width * self.__height

    def display(self):
        """ method doc """
        for a in range(self.__y):
            print("")
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ method doc """
        s = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        return f"{s} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.integer_validator("width", args[1])
                self.width = args[1]
            if len(args) >= 3:
                self.integer_validator("height", args[2])
                self.height = args[2]
            if len(args) >= 4:
                self.integer_validator("x", args[3])
                self.x = args[3]
            if len(args) >= 5:
                self.integer_validator("y", args[4])
                self.y = args[4]

        if not args and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                else:
                    self.integer_validator(key, value)
                    if key == "width":
                    self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
