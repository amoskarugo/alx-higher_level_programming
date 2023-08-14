#!/usr/bin/python3.8


def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = []
    for i in range(len(my_list)):
        new_list.append(True if my_list[i] % 2 == 0 else False)
    return new_list
