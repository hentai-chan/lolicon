#!/usr/bin/env python3

"""
Cryptography
============

TODO: Write namespace description.
"""

import math
import string
from random import randint
from typing import Tuple

from .. import utils
from ..mathematics import gcd, mod_inverse
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
def encrypt_morse_code(msg: str) -> str:
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

def decrypt_morse_code(cypher: str) -> str:
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

    Notes
    -----
    - The ROT13 cypher is a special case of the caesar cypher (set `shift=13`)
    - A slightly stronger cypher can be obtained by using a shuffled `seed`
    - This cypher's weakness is proportional to `len(msg)`, i.e. longer messages 
    are easier to break (the unicity distance of English equals 27.6 letters of
    cypher text for a simple substitution using a mixed alphabet as seed)

    References
    ----------
    - <https://en.wikipedia.org/wiki/Caesar_cipher>
    - <https://en.wikipedia.org/wiki/Substitution_cipher>
    """
    return msg.translate(str.maketrans(seed, ''.join((seed[shift%len(seed):], seed[:shift%len(seed)]))))

def decrypt_caesar_cypher(cypher: str, shift: int=3, seed: str=string.ascii_uppercase) -> str:
    """
    Decrypt a in ceasar cypher encrypted message. Note that you have to pass the same `seed`
    that you used to encrypt the original message.
    """
    return cypher.translate(str.maketrans(''.join((seed[shift%len(seed):], seed[:shift%len(seed)])), seed))

@utils.raise_warning(__warning_msg)
def encrypt_transposition_cypher(msg: str, key: int) -> str:
    """
    Encrypt a message using the transposition cypher. This encryption method
    turns a message into a matrix, whose column characters are joined from top
    to bottom. Those sub-strings are joined by row in turn again. Messages of
    uneven length are padded by `-`, though these placeholder are skipped by the
    algorithm.

    Example
    -------
    Arguments: `msg='Common sense is not so common.'` and `key=8`. The number of
    rows equals `keys`.
    ```
    [0] [1] [2] [3] [4] [5] [6] [7]
     C   o   m   m   o   n       s  [0]
     e   n   s   e       i   s      [1]
     n   o   t       s   o       c  [2]
     o   m   m   o   n   .   -   -  [3]
    ```
    Reading each column from top to bottom starting by the left-most row, the
    cypher becomes `Cenoonommstmme oo snnio. s s c`.

    Notes
    -----
    - This encryption methods doesn't work, if `key >= len(msg)`
    - The encryption becomes weaker if `key` is not much smaller than `len(msg)`
    - Hence, the magnitude of possible keys makes this method vulnerable for
    brute force attacks if `msg` is not very long
    - There are about `range(2, len(seed))` possible key combinations for this cypher
    """
    cypher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(msg):
            cypher[col] += msg[pointer]
            pointer += key
    return ''.join(cypher)

def decrypt_transposition_cypher(cypher: str, key: int) -> str:
    """
    Decrypt a message by using the transposition cypher by calculating the number
    of columns required to encrypt the original message and by taking into account
    occurring placeholder characters (`-`) to prevent index out of range errors.
    """
    num_of_col = math.ceil(len(cypher) / key)
    source = [''] * num_of_col
    col, row = 0, 0
    for char in cypher:
        source[col] += char
        col += 1
        if (col == num_of_col) or (col == num_of_col - 1 and row >= key - ((num_of_col * key) - len(cypher))):
            col = 0
            row += 1
    return ''.join(source)

def __split_affine_key(key: int, seed: str) -> Tuple[int, int]:
    return (key // len(seed), key % len(seed))

def __validate_affine_keys(key1: int, key2: int, seed: str) -> None:
    if key1 == 1 or key2 == 0:
        logger.error(f"First check failed: extremely insecure key combination for {key1=}, {key2=}")
        raise ValueError(f"The affine cypher becomes extremely vulnerable when {key1=} or {key2=}.")

    if key1 < 0 or key2 < 0 or key2 > len(seed) - 1:
        logger.error(f"Second check failed: invalid key range for {key1=}, {key2=}, {len(seed)=}")
        raise ValueError(f"{key1=} must be greater than 0 and {key2=} must be between 0 and {len(seed)-1}.")

    if gcd(key1, len(seed)) != 1:
        logger.error(f"Third check failed: {key1=} and {len(seed)=} are not relatively prime")
        raise ValueError(f"{key1=} and {len(seed)=} are not relatively prime.")

def generate_affine_key(seed: str=string.printable) -> int:
    """
    Generate a new key for the affine cypher encryption algorithm.
    """
    seed_len = len(seed)
    while True:
        key1, key2 = randint(2, seed_len), randint(2, seed_len)
        if gcd(key1, seed_len) == 1:
            return key1 * seed_len + key2

@utils.raise_warning(__warning_msg)
def encrypt_affine_cypher(msg: str, key: int, seed: str=string.printable) -> str:
    """
    Encrypt a message using the affine cypher. The affine cypher is a combination
    of the multiplicative cypher and the caesar cypher. Because the multiplicative
    cypher always maps the first character onto itself, another encryption method
    is applied immediately after the multiplicative cypher. Since the first key
    must be relatively prime to the seed length, not every key qualifies for this
    encryption method. For this reason, use the `generate_affine_key` method to
    create a key.

    Example
    -------
    ```
    >>> from lolicon.compsci import cryptography as crypto
    >>> key = crypto.generate_affine_key()
    >>> msg = "Hello, World!"
    >>> cypher = crypto.encrypt_affine_cypher(msg, key)
    >>> print(msg == crypto.decrypt_affine_cypher(cypher, key))
    True
    ```

    Notes
    -----
    - The seed dictates language support
    - Using the default seed (`len(seed)=100`), there are `key1 * key2 = 100 * 100 = 10000`
    key combinations to crack this cypher
    """
    key1, key2 = __split_affine_key(key, seed)
    __validate_affine_keys(key1, key2, seed)
    encrypt = lambda char: seed[(seed.find(char) * key1 + key2) % len(seed)]
    return ''.join((encrypt(char) if char in seed else char for char in msg))

def decrypt_affine_cypher(cypher: str, key: int, seed: str=string.printable) -> str:
    """
    Decrypt an affine cypher encrypted message. Note that you need both, the key
    and seed, to decypher a message.
    """
    key1, key2 = __split_affine_key(key, seed)
    __validate_affine_keys(key1, key2, seed)
    decrypt = lambda char: seed[(seed.find(char) - key2) * mod_inverse(key1, len(seed)) % len(seed)]
    return ''.join((decrypt(char) if char in seed else char for char in cypher))


@utils.raise_warning(__warning_msg)
def encrypt_vigenere_cypher(msg: str) -> str:
    """
    TODO: write doc string + write implementation
    """
    raise NotImplementedError()

def decrypt_vigenere_cypher(cypher: str) -> str:
    """
    TODO: write doc string + write implementation
    """
    raise NotImplementedError()
