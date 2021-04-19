#!/usr/bin/env python3

import string
import unittest

import pytest
import src.lolicon.compsci as compsci
from src.lolicon.compsci import cryptography as crypto


class TestComputerScience(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_bin2dec(self):
        self.assertEqual(compsci.bin2dec('10110'), 22)
        self.assertEqual(compsci.bin2dec('100110111'), 311)
        self.assertEqual(compsci.bin2dec('1101101101011'), 7019)

    def test_dec2bin(self):
        self.assertEqual(compsci.dec2bin(22), '00010110')
        self.assertEqual(compsci.dec2bin(311, padding=10), '0100110111')
        self.assertEqual(compsci.dec2bin(7019, padding=16), '0001101101101011')

    def test_dec2oct(self):
        self.assertEqual(compsci.dec2oct(22), '26')
        self.assertEqual(compsci.dec2oct(311), '467')
        self.assertEqual(compsci.dec2oct(7019), '15553')

    def test_oct2dec(self):
        self.assertEqual(compsci.oct2dec('26'), 22)
        self.assertEqual(compsci.oct2dec('467'), 311)
        self.assertEqual(compsci.oct2dec('15553'), 7019)

    def test_dec2hex(self):
        self.assertEqual(compsci.dec2hex(22), '16')
        self.assertEqual(compsci.dec2hex(311), '137')
        self.assertEqual(compsci.dec2hex(7019), '1B6B')

    def test_hex2dec(self):
        self.assertEqual(compsci.hex2dec('16'), 22)
        self.assertEqual(compsci.hex2dec('137'), 311)
        self.assertEqual(compsci.hex2dec('1B6B'), 7019)

class TestCryptography(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_morse_code(self):
        from_morse = lambda msg: msg.upper().replace(' ', '')
        # case-insensitive
        msg = 'Measure what is measurable and make measurable what is not so'
        cypher = crypto.encrypt_morse_code(msg)
        self.assertEqual(crypto.decrypt_morse_code(cypher), from_morse(msg))
        # numeric support
        msg = 'I was x years old in the year x2'
        cypher = crypto.encrypt_morse_code(msg)
        self.assertEqual(crypto.decrypt_morse_code(cypher), from_morse(msg))        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_binary(self):
        msg = "It's not that I'm so smart, it's just that I stay with problems longer."
        cypher = crypto.encrypt_binary(msg)
        self.assertEqual(crypto.decrypt_binary(cypher), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_base64(self):
        # test padding
        msg = "Hello, World!"
        self.assertEqual(crypto.encrypt_base64(msg), 'SGVsbG8sIFdvcmxkIQ==')
        # check msg retention 
        msg = "Man is distinguished, not only by his reason, but ..."
        cypher = crypto.encrypt_base64(msg)
        self.assertEqual(crypto.decrypt_base64(cypher), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_caesar_cypher(self):
        # default seed
        msg = 'mathematics is the handwriting on the human consciousness of the very spirit of life itself.'
        cypher = crypto.encrypt_caesar_cypher(msg, shift=2)
        self.assertEqual(crypto.decrypt_caesar_cypher(cypher, shift=2), msg)
        # uppercase only
        msg = 'THERE ARE NO CREEDS IN MATHEMATICS'
        cypher = crypto.encrypt_caesar_cypher(msg, shift=8,seed=string.ascii_uppercase)
        self.assertEqual(crypto.decrypt_caesar_cypher(cypher, shift=8, seed=string.ascii_uppercase), msg)
        # using special characters and numbers
        seed = ''.join((string.ascii_letters, string.digits, string.punctuation))
        msg = 'Mathematics is not a contemplative but a creative subject.'
        cypher = crypto.encrypt_caesar_cypher(msg, shift=13, seed=seed)
        self.assertEqual(crypto.decrypt_caesar_cypher(cypher, shift=13, seed=seed), msg)        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_transposition_cypher(self):
        msg = 'The highest form of pure thought is in mathematics.'
        cypher = crypto.encrypt_transposition_cypher(msg, key=8)
        self.assertEqual(crypto.decrypt_transposition_cypher(cypher, key=8), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_affine_cypher(self):
        key = crypto.generate_affine_key()
        msg = 'The important thing to remember about mathematics is not to be frightened.'
        cypher = crypto.encrypt_affine_cypher(msg, key)
        self.assertEqual(crypto.decrypt_affine_cypher(cypher, key), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_vigenere_cypher(self):
        # default settings
        key = 'jacqueline'
        msg = 'mathematics is the music of reason'
        cypher = crypto.encrypt_vigenere_cypher(msg, key)
        self.assertEqual(crypto.decrypt_vigenere_cypher(cypher, key), msg)
        # shuffled key with extended seed
        key = string.printable
        sorted(key)
        msg = "Go down deep enough into anything and you will find mathematics."
        cypher = crypto.encrypt_vigenere_cypher(msg, key, string.printable)
        self.assertEqual(crypto.decrypt_vigenere_cypher(cypher, key, string.printable), msg)