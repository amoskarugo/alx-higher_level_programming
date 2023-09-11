#!/usr/bin/python3
"""Geometry class module"""


class BaseGeometry:
    """A base class for geometry-related operations"""
    def __init__(self):
        pass

    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks whether the value passed is an integer.

        Args:
            name (string): name of the integer to be passed
            value (int): parameter to check whether it is an integer

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
