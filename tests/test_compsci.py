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

    def test_bin2dec(self):
        self.assertEqual(compsci.dec2bin(22), '10110')
        self.assertEqual(compsci.dec2bin(311), '100110111')
        self.assertEqual(compsci.dec2bin(7019), '1101101101011')

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
        source = 'Hello World'
        cypher = cryptography.encrypt_morse_code(source)
        self.assertEqual(cryptography.decrypt_morse_code(cypher), from_morse(source))
        # numeric support
        source = 'The attack takes place at 2 AM'
        cypher = cryptography.encrypt_morse_code(source)
        self.assertEqual(cryptography.decrypt_morse_code(cypher), from_morse(source))        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_caesar_cypher(self):
        # default seed
        source = 'HELLO WORLD'
        cypher = cryptography.encrypt_caesar_cypher(source, shift=8)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=8), source)
        # lowercase only
        source = 'help me i am insecure'
        cypher = cryptography.encrypt_caesar_cypher(source, shift=2, seed=string.ascii_lowercase)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=2, seed=string.ascii_lowercase), source)
        # using special characters and numbers
        seed = ''.join((string.ascii_letters, string.digits, string.punctuation))
        source = 'I sure hope no one will read this message!'
        cypher = cryptography.encrypt_caesar_cypher(source, shift=13, seed=seed)
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=13, seed=seed), source)        

    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_transposition_cypher(self):
        source = 'Common sense is not so common.'
        cypher = cryptography.encrypt_transposition_cypher(source, key=8)
        self.assertEqual(cryptography.decrypt_transposition_cypher(cypher, key=8), source)
        