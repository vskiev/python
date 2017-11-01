#!/usr/bin/python3

import unittest
from testing import test_me


class TestMeTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(test_me([[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]), 72)

    def test_2(self):
        self.assertEqual(test_me([[[[[[[[[[[1, 11, 111]]]]]]]]]]]), 123)

    def test_3(self):
        self.assertEqual(test_me([1, 2, 3, 4, 5]), 15)

    def test_4(self):
        self.assertEqual(test_me([1, 2, 3]), 6)