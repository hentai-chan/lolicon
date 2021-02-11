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

    Example
    -------
    ```
    H >> ...., E >> ., L >> .-.., O >> ---
    ```
    Hence, `HELLO = .... . .-.. .-.. ---`.

    References
    ----------
    - <https://en.wikipedia.org/wiki/Morse_code>
    """
    try:
        return ' '.join((__morse_code[char if char.isdigit() else char.upper()] for char in msg.replace(' ', '')))
    except KeyError:
        logger.error(f"Original message contained illegal characters: {msg=}")
        raise ValueError(f"You may only use {','.join(string.ascii_letters)} and {','.join(string.digits)} in your message.")

def decrypt_morse(cypher: str) -> str:
    """
    Decrypt a in morse encrypted message by using the ITU standard. The resulting
    message will be in uppercase and stripped off all whitespaces.
    """
    translate = {value: key for key, value in __morse_code.items()}
    return ''.join(translate[char] for char in cypher.split(' '))

@utils.raise_warning(__warning_msg)
def encrypt_caesar_cypher(msg: str, shift: int=3, seed: str=string.ascii_uppercase) -> str:
    """
    Decrypt a message by using the ceasar chipher that employs a substitution method
    and replaces each character by a fix number of positions (so called `shift`).

    Example
    -------
    ```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
    ```
    Using the default argument yields the following correspondence:
    ```
    H >> E, E >> B, L >> I, O >> L
    ```
    Hence, `HELLO = EBIIL` for `shift=3`.

    References
    ----------
    - <https://en.wikipedia.org/wiki/Caesar_cipher>
    """
    return msg.translate(str.maketrans(seed, ''.join((seed[shift%len(seed):], seed[:shift%len(seed)]))))

def decrypt_caesar_cypher(cypher: str, shift: int=3, seed: str=string.ascii_uppercase) -> str:
    """
    Decrypt a in ceasar cypher encrypted message. Note that you have to pass the same `seed`
    that you used to encrypt the original message.
    """
    return cypher.translate(str.maketrans(''.join((seed[shift%len(seed):], seed[:shift%len(seed)])), seed))

def encrypt_transposition_cypher(msg: str, key: int) -> str:
    raise NotImplementedError()

def decrypt_transposition_cypher(cypher: str, key: int) -> str:
    raise NotImplementedError()