#!/usr/bin/python3.8

def best_score(a_dictionary):
    high_score = 0
    key = ""
    if not a_dictionary:
        return None
    for i, j in a_dictionary.items():
        if j > high_score:
            high_score = j
    for x in a_dictionary:
        if a_dictionary[x] == high_score:
            key = x
    return key
