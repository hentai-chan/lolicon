#!/usr/bin/env python3

import unittest

from src.lolicon.mathematics import mathematics

class Mathematics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_gcd(self):
        self.assertEqual(mathematics.gcd(60, 48), 12)
        self.assertEqual(mathematics.gcd(32, 24), 8)
        self.assertEqual(mathematics.gcd(12121, 37847374), 23)

    def test_mod_inverse(self):
        self.assertEqual(mathematics.mod_inverse(5, 7), 3)
        self.assertEqual(mathematics.mod_inverse(763, 23), 6)
        self.assertEqual(mathematics.mod_inverse(9438274, 40928773), 40286876)

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(mathematics.sieve_of_eratosthenes(12), [2, 3, 5, 7, 11])
        self.assertEqual(mathematics.sieve_of_eratosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
