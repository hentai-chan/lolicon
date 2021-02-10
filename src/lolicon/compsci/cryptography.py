#!/usr/bin/env python3

import string

from .. import utils
from ..utils import logger

__warning_msg = "You're using an cryptographically insecure method."

# international morse code map suitable for english correspondence
__morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '......',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

@utils.raise_warning(__warning_msg)
def encrypt_morse(msg: str) -> str:
    """
    Encrypt a message into morse code using the ITU standard. List of supported
    characters includes all ASCII letters as well as integers.
    """
    try:
        return ' '.join((__morse_code[char if char.isdigit() else char.upper()] for char in msg.replace(' ', '')))
    except KeyError:
        logger.error(f"Original message contained illegal characters: {msg=}")
        raise ValueError(f"You may only use {','.join(string.ascii_letters)} and {','.join(string.digits)} in your message.")

def decrypt_morse(cypher: str) -> str:
    """
    Decrypt a in morse encrypted message. The resulting message will be in upper
    case and stripped off all whitespaces.
    """
    translate = {value: key for key, value in __morse_code.items()}
    return ''.join(translate[char] for char in cypher.split(' '))
