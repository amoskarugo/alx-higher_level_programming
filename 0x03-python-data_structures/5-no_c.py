#!/usr/bin/python3.8

def no_c(my_string):
    if not my_string:
        return
    new_string = ""

    for char in my_string:
        if char in "cC":
            continue
        new_string += char
    return new_string
