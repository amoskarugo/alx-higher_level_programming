#!/usr/bin/python3.8

"""Class Square defination."""


class Square:
    """Rpresents class square."""

    def __init__(self, size=0):
        self.size = size
        """Initialization of a new Square.
        Args:
            size (int): size of square
        """

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square"""
        return (self.__size) * (self.__size)

    def my_print(self):
        """prints a square on stdout"""
        s = self.size
        for i in range(s):
            for i in range(s):
                print("#", end="")
            print()
        if s == 0:
            print()
