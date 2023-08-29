#!/usr/bin/python3.8

"""Class Square defination."""


class Square:
    """Rpresents class square."""
    def __init__(self, size=0):
        """Initialization of a new Square.
        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of square"""
        return (self.__size) * (self.__size)
