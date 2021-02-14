#!/usr/bin/env python3

import math
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


@utils.raise_warning(__warning_msg)
def encrypt_vigenere_cypher():
    raise NotImplementedError()

def decrypt_vigenere_cypher():
    raise NotImplementedError()
