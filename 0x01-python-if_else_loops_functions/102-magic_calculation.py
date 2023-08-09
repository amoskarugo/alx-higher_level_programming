#!/usr/bin/python3.8

def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
