#!/usr/bin/python3.8

def print_sorted_dictionary(a_dictionary, key, value):
    for i, j in sorted(a_dictionary.items()):
        if i == key:
            a_dictionary[i] = value
        else:
            a_dictionary[key] = value
    return a_dictionary
