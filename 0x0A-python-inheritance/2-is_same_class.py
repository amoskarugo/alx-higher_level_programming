#!/usr/bin/python3.8
"""function to check for instance"""


def is_same_class(obj, a_class):
    """checks whether the object is as instance of a class

    Args:
        obj (object): an object
        a_class (class): class
    Return:
        True if object is an instance of the class else false.
    """
    return type(obj) is a_class
