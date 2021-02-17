#!/usr/bin/env python3

import string
import unittest

import pytest
import src.lolicon.compsci as compsci
from src.lolicon.compsci import cryptography


class ComputerScience(unittest.TestCase):
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
        self.assertEqual(compsci.dec2bin(311, pad_zero=10), '0100110111')
        self.assertEqual(compsci.dec2bin(7019, pad_zero=16), '0001101101101011')

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
        msg = 'Hello World'
        cypher = cryptography.encrypt_morse_code(msg)
        self.assertEqual(cryptography.decrypt_morse_code(cypher), from_morse(msg))
        # numeric support
        msg = 'The attack takes place at 2 AM'
        cypher = cryptography.encrypt_morse_code(msg)
        self.assertEqual(cryptography.decrypt_morse_code(cypher), from_morse(msg))        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_encrypt_binary(self):
        msg = 'Hello, World!'
        cypher = cryptography.encrypt_binary(msg)
        self.assertEqual(cryptography.decrypt_binary(cypher), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_caesar_cypher(self):
        # default seed
        msg = 'HELLO WORLD'
        cypher = cryptography.encrypt_caesar_cypher(msg, shift=8)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=8), msg)
        # lowercase only
        msg = 'help me i am insecure'
        cypher = cryptography.encrypt_caesar_cypher(msg, shift=2, seed=string.ascii_lowercase)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=2, seed=string.ascii_lowercase), msg)
        # using special characters and numbers
        seed = ''.join((string.ascii_letters, string.digits, string.punctuation))
        msg = 'I sure hope no one will read this message!'
        cypher = cryptography.encrypt_caesar_cypher(msg, shift=13, seed=seed)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=13, seed=seed), msg)        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_transposition_cypher(self):
        msg = 'Common sense is not so common.'
        cypher = cryptography.encrypt_transposition_cypher(msg, key=8)
        self.assertEqual(cryptography.decrypt_transposition_cypher(cypher, key=8), msg)

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_affine_cypher(self):
        key = cryptography.generate_affine_key()
        msg = 'A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.'
        cypher = cryptography.encrypt_affine_cypher(msg, key)
        self.assertEqual(cryptography.decrypt_affine_cypher(cypher, key), msg)
