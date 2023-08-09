#!/usr/bin/python3.8

def remove_char_at(str, n):
    new_str = ""

    for char in range(len(str)):
        if char == n:
            continue
        new_str = new_str + str[char]
    return new_str
