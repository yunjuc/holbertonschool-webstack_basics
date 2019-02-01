#!/usr/bin/python3
import unittest
max_integer = __import__('16-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test max_integer'''

    def test_normal(self):
        '''test a normal list'''
        res = max_integer([1, 3, 3, 2])
        self.assertEqual(res, 3)

    def test_empty_list(self):
        '''test empty list'''
        res = max_integer([])
        self.assertEqual(res, None)

    def test_negetive(self):
        '''test list with negative int'''
        res = max_integer([19, -3, -45, 27])
        self.assertEqual(res, 27)

    def test_float(self):
        '''test float numbers'''
        res = max_integer([0, 4, 7.0])
        self.assertEqual(res, 7)

    def test_first(self):
        '''test max at the beginning'''
        res = max_integer([99, 34, 8])
        self.assertEqual(res, 99)

    def test_last(self):
        '''test max at the end'''
        res = max_integer([0, 5, 99])
        self.assertEqual(res, 99)

    def test_one_element(self):
        '''test only one element'''
        res = max_integer([9])
        self.assertEqual(res, 9)
