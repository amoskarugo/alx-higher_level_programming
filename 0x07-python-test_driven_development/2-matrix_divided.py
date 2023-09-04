#!/usr/bin/python3.8


"""
    function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        divide all the alements of a matrix by div

        Args:
            matrix (list): a list of elements
            div (int): a divider
        Returns:
            a new matrix after the dision operation

    """
    new_list = []

    if not matrix or not matrix[0][0]:
        raise IndexError("list index out of range")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if ((not isinstance(div, int)) and (not isinstance(div, float))):
        raise TypeError("div must be a number")

    len_row = len(matrix[0])

    for i in matrix:
        if len(i) != len_row:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for col in row:
            if ((not isinstance(col, int) and (not isinstance(col, float)))):
                raise TypeError("matrix must be a matrix(list of lists)
                                of integers/floats")

    new_list = list(map(lambda x: list(map(lambda i:
                    round(i/div, 2), x)), matrix))

    return new_list
