#!/usr/bin/python3.8

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    list_len = len(my_list) - 1
    if idx > list_len:
        return my_list

    my_list[idx] = element
