#!/usr/bin/python3.8


def divisible_by_2(my_list=[]):
    if not my_list:
        return
    for i in range(len(my_list)):
        my_list[i] = True if my_list[i] % 2 == 0 else False
    return my_list
