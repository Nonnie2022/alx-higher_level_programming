#!/usr/bin/python3

class BaseGeometry:
    """ BaseGeometry class """

    def integer_validator(self, name, value):
        """ validate positive integer value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns a string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

