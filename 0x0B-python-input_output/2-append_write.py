#!/usr/bin/python3.8
"""module that handles appending into a file."""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        appended = f.write(text)
    return appended
