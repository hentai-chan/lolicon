import unittest

import src.lolicon.compsci as compsci
from src.lolicon.compsci import cryptography

class ComputerScience(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def test_bin2dec(self):
        self.assertEqual(compsci.bin2dec('10110'), 22)
        self.assertEqual(compsci.bin2dec('100110111'), 311)
        self.assertEqual(compsci.bin2dec('1101101101011'), 7019)

    def test_bin2dec(self):
        self.assertEqual(compsci.dec2bin(22), '10110')
        self.assertEqual(compsci.dec2bin(311), '100110111')
        self.assertEqual(compsci.dec2bin(7019), '1101101101011')

class TestCryptography(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ...

    @classmethod
    def tearDownClass(cls):
        ...

    def test_hello_world(self):
        self.assertEqual(cryptography.hello_world(surpress_warning=True), 'Hello, World!')