#!/usr/bin/python3.8
"""module to write into a file"""


def write_file(filename="", text=""):
    """function that writes into a file a returns
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        written = f.write(text)

    return written
