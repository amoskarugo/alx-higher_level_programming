#!/usr/bin/python3

"""class MyInt that inherits from int"""


class MyInt(int):
    """A subclass of class int"""
    def __eq__(self, other):
        """change the behaviour of == to !="""
        return int(self) != other

    def __ne__(self, other):
        """change behavior of != to =="""
        return int(self) == other
