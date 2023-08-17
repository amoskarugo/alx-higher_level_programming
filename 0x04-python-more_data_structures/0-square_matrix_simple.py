#!/usr/bin/python3.8


def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = matrix[:]

    squared = list(map(lambda x: list(map(lambda i: i ** 2, x)), new_matrix))

    return squared
