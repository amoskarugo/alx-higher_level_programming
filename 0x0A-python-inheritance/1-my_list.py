#!/usr/bin/python3.8


"""1-list class module"""


class MyList(list):
    """list subclsaa"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
