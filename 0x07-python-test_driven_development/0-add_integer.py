#!/usr/bin/python3.8

"""
    fuction to add two integers
    add_integer(1, 3)
    4
"""


def add_integer(a, b=98):
    """A fuction that add two integrs.

    Args:
        a (int): first number.
        b (int): second number.
    Return:
        sum of two numbers
    Raises:
        TypeError: if a or be are neither int or float

    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
