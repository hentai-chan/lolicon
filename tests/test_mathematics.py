#!/usr/bin/env python3

import unittest

from src.lolicon.mathematics import mathematics

class ComputerMathematics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_gcd(self):
        self.assertEqual(mathematics.gcd(60, 48), 12)
        self.assertEqual(mathematics.gcd(32, 24), 8)
