#!/usr/bin/python3
"""unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmax_integer(unittest.TestCase):
    '''max_integer unittest class'''
    def test_mod_docstring(self):
        '''tests for module docstring'''
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_func_docstring(self):
        '''tests for function docstring'''
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_noarguments(self):
        '''tests for no arguments passed'''
        self.assertIsNone(max_integer())

    def test_oneinteger(self):
        '''tests for only integer in the list'''
        list = [4]
        self.assertEqual(max_integer(list), 4)

    def test_emptylist(self):
        '''tests for an empty list'''
        list = []
        self.assertIsNone(max_integer(list))

    def test_negative(self):
        '''tests Negative integers as arguments'''
        list = [-2, -4, -19, -57]
        self.assertEqual(max_integer(list), -2)

    def test_positive(self):
        '''tests max of positive integers'''
        list = [4, 7, 27, 91, 13]
        self.assertEqual(max_integer(list), 91)

    def test_positive_negative(self):
        '''tests max of a list with both positive an negative ints'''
        list = [1, 4, -8, 3, -19, 7]
        self.assertEqual(max_integer(list), 7)

    def test_nonint_args(self):
        '''tests list with arguments that are not all integers'''
        list = ['int', 4, 2, 9, -2.7]
        with self.assertRaises(TypeError):
            max_integer(list)

    def test_None(self):
        '''tests None as an argument'''
        list = [None]
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ = "__main__":
    unittest.main()

