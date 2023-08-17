#!/usr/bin/python3.8


def uniq_add(my_list=[]):
    uniq_vals = set(my_list)

    total = 0
    for num in uniq_vals:
        total += num
    return total
