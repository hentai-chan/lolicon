import string
import unittest

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

    def test_encrypt_morse(self):
        # case-insensitive
        source = 'Hello World'
        cypher = '.... . .-.. .-.. --- .-- --- .-. .-.. -..'
        self.assertEqual(cryptography.encrypt_morse(source), cypher)
        # numeric support
        source = 'The attack takes place at 2 AM'
        cypher = '- .... . .- - - .- -.-. -.- - .- -.- . ... .--. .-.. .- -.-. . .- - ..--- .- --'
        self.assertEqual(cryptography.encrypt_morse(source), cypher)

    def test_decrypt_morse(self):
        # result always in uppercase without stripped off all whitespaces
        source = 'HELLOWORLD'
        cypher = '.... . .-.. .-.. --- .-- --- .-. .-.. -..'
        self.assertEqual(cryptography.decrypt_morse(cypher), source)
        source = 'THEATTACKTAKESPLACEAT2AM'
        cypher = '- .... . .- - - .- -.-. -.- - .- -.- . ... .--. .-.. .- -.-. . .- - ..--- .- --'
        self.assertEqual(cryptography.decrypt_morse(cypher), source)

    def test_encrypt_caesar_cypher(self):
        # default seed
        source = 'THE SECRET PASSWORD IS ROSEBUD'
        cypher = 'BPM AMKZMB XIAAEWZL QA ZWAMJCL'
        self.assertEqual(cryptography.encrypt_caesar_cypher(source, shift=8), cypher)
        # lowercase only
        source = 'the crazy programmer'
        cypher = 'vjg etcba rtqitcoogt'
        self.assertEqual(cryptography.encrypt_caesar_cypher(source, shift=2, seed=string.ascii_lowercase), cypher)
        # using special characters and numbers
        seed = ''.join((string.ascii_letters, string.digits, string.punctuation))
        source = 'Hello, World!'
        cypher = 'UryyB] 9BEyq.'
        self.assertEqual(cryptography.encrypt_caesar_cypher(source, shift=13, seed=seed), cypher)

    def test_decrypt_caesar_cypher(self):
        # default seed
        source = 'THE SECRET PASSWORD IS ROSEBUD'
        cypher = 'BPM AMKZMB XIAAEWZL QA ZWAMJCL'
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=8), source)
        # lowercase only
        source = 'the crazy programmer'
        cypher = 'vjg etcba rtqitcoogt'
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=2, seed=string.ascii_lowercase), source)
        # using special characters and numbers
        seed = ''.join((string.ascii_letters, string.digits, string.punctuation))
        source = 'Hello, World!'
        cypher = 'UryyB] 9BEyq.'
        self.assertEqual(cryptography.decrypt_caesar_cypher(cypher, shift=13, seed=seed), source)
