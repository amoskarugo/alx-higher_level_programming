#!/usr/bin/python3.8

"""
    function to print two strings
"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints first and second name

    Args:
        first_name(string): first name
        last_name(string): last name
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
