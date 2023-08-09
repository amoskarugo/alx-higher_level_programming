#!/usr/bin/python3.8

def remove_char_at(str, n):
    new_str = ""

    for l in range(len(str)):
        if l == n:
            continue
        new_str = new_str + str[l]
    return new_str
