#!/usr/bin/python3.8

"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Testcase for the max_integer function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([7, 8, 76, 200]), 200)

    def test_empty_list(self):
        """ Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_the_end(self):
        """Test a list where max value is at the end"""
        _end = [1, 3, 2, 33]
        self.assertEqual(max_integer(_end), 33)

    def test_max_start(self):
        """Test a list with a beginning max value."""
        _start = [78, 19, 3, 2]
        self.assertEqual(max_integer(_start), 78)

    def ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [100, 200, 300, 400]
        self.assertEqual(max_integer(ordered), 400)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [100, 200, 400, 300]
        self.assertEqual(max_integer(unordered), 400)

    def test_single_element(self):
        """Test a list with a single element."""
        _element = [40]
        self.assertEqual(max_integer(_element), 40)

    def test_ints_and_floats_list(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_float_list(self):
        """Test a list of floats."""
        _float = [1.53, 6.33, -9.123, 17.2, 6.0]
        self.assertEqual(max_integer(_float), 17.2)

    def test_string_list(self):
        """Test a string."""
        string = "amos"
        self.assertEqual(max_integer(string), 's')

    def test_neg_float_list(self):
        """Test negative floats"""
        neg_float = [-5.55, -66.66, -111.1]
        self.assertEqual(max_integer(neg_float), -5.55)

    def test_diff_datatypes(self):
        """ Test different data types"""
        with self.assertRaises(TypeError):
            max_integer([17, "x"])

    def test_listOflist(self):
        """ Test nested list"""
        matrix = [[1, 2], [8, 9]]
        self.assertEqual(max_integer(matrix), [8, 9])
