#!/usr/bin/python3.8
"""module that handles appending into a file."""


def append_write(filename="", text=""):
    """function that appends into the file and returns
       the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        appended = f.write(text)
    return appended
