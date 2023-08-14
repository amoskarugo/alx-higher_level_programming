#!/usr/bin/python3.8

def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = ()

    tup_a = tuple_a + (0, 0)
    tup_b = tuple_b + (0, 0)

    new_tup = tup_a[0] + tup_b[0], tup_a[1] + tup_b[1]
    return new_tup
