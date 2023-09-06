#!/usr/bin/python3.8


"""
    class Rectangle
"""


class Rectangle:
    """
        Defines REctangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(sel):
        return (self.height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigh must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
