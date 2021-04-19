#!/usr/bin/env python3

"""
Cryptography
============

Preamble
-----

Cryptography is the art and science of concealing messages in order to introduce
a level of secrecy between two parties (namely sender and receiver) to keep the
communication channel secure. This namespace implements historically important
encryption methods that are, by and large, cryptographically insecure. Their
implementation is solely provided for educational purposes only.

Note
----
All encryption methods encompass doc strings that detail the inner workings of
their algorithm briefly. Note sections highlight interesting properties and further
explain circumstantial weaknesses and relative strengths for certain parameters.

References
----------
- "A Beginner's Guide to Cryptography and Computer Programming with Python" by Al Sweigart

"""

import math
import string
from random import randint
from textwrap import wrap
from typing import Tuple

from lolicon import compsci

from .. import utils
from ..compsci import bin2dec, dec2bin
from ..mathematics import gcd, mod_inverse
from ..utils import logger

__warning_msg = "You're using an cryptographically insecure method."

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

__base64_table = ''.join((string.ascii_uppercase, string.ascii_lowercase, string.digits, '+', '/'))

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

    Notes
    -----
    - This encryption method only works with letters from the English alphabet

    References
    ----------
    - <https://en.wikipedia.org/wiki/Morse_code>
    """
    try:
        return ' '.join((__morse_code[char if char.isdigit() else char.upper()] for char in msg.replace(' ', '')))
    except KeyError:
        logger.error(f"Original message contained illegal characters: {msg=}", exc_info=True)
        raise ValueError(f"You may only use {','.join(string.ascii_letters)} and {','.join(string.digits)} in your message.")

def decrypt_morse_code(cypher: str) -> str:
    """
    Decrypt a in morse encrypted message by using the ITU standard. The resulting
    message will be in uppercase and stripped off all whitespaces.
    """
    translate = {value: key for key, value in __morse_code.items()}
    return ''.join(translate[char] for char in cypher.split(' '))

@utils.raise_warning(__warning_msg)
def encrypt_binary(msg: str) -> str:
    """
    Encrypt a message into a sequence of binary numbers. Computers store characters
    as number by using standardized character encoding systems. Since python uses
    UTF-8 as default character code map, that's what is also used in this encryption
    method.

    ASCII Table
    -----------
    ```
    A=65  I=73  Q=81  Y=89
    B=66  J=74  R=82  Z=90
    C=67  K=75  S=83
    D=68  L=76  T=84
    E=69  M=77  U=85
    F=70  N=78  V=86
    G=71  O=79  W=87
    H=72  P=80  X=88
    ```

    Binary Encoding
    ---------------
    ```
    65=01000001  73=01001001  81=01010001   89=01011001
    66=01000010  74=01001010  82=01010010   90=01011010
    67=01000011  75=01001011  83=01010011
    68=01000100  76=01001100  84=01010100
    69=01000101  77=01001101  85=01010101
    70=01000110  78=01001110  86=01010110
    71=01000111  79=01001111  87=01010111
    72=01001000  80=01010000  88=01011000
    ```

    Encrypting a 'HELLO' into binary results in
    ```
      H=72     E=69     L=76     L=76     0=79
    01001000 01000101 01001100 01001100 01001111
    ```

    References
    ----------
    - <https://en.wikipedia.org/wiki/Character_encoding>
    - <https://en.wikipedia.org/wiki/Binary_number>
    """
    return ' '.join((dec2bin(ord(char)) for char in msg))

def decrypt_binary(cypher: str) -> str:
    """
    Decrypts a binary message by mapping their value to UTF-8.
    """
    return ''.join((chr(bin2dec(char)) for char in cypher.split()))

@utils.raise_warning(__warning_msg)
def encrypt_base64(msg: str) -> str:
    """
    Encrypts a message into a base64 string using MIME's Base64 implementation.
    It takes an ASCII sequence `msg` as parameter and divides the culminating
    binary string into groups of 6 bits. Their values are mapped to a `__base64_table`.
    Cyphers that are not a multiple of 4 are padded with the `=` character to the
    right.

    Encoding Process
    ----------------
    ```
       M         A          N           ASCII MSG
    01001101, 01100001, 01101110        1-BYTE SEQUENCES
    
    010011, 010110, 000101, 101110      6-BIT SEQUENCES
       T       W       F       u        BASE64 TABLE
    ```
    """
    buffer = wrap(''.join((compsci.dec2bin(ord(c)) for c in msg)), 6)
    cypher = ''.join((__base64_table[compsci.bin2dec(bin_.ljust(6, '0'))] for bin_ in buffer))
    return cypher if len(cypher) % 4 == 0 else cypher.ljust(len(cypher) + 4 - (len(cypher) % 4), '=')

def decrypt_base64(cypher: str) -> str:
    """
    Decrypt a base64 encrypted message using MIME's Base64 implementation.
    """
    buffer = (compsci.dec2bin(__base64_table.index(v), padding=6) for v in cypher.strip('='))
    bin_stream = wrap(''.join(buffer), 8)
    return ''.join(chr(compsci.bin2dec(bin_)) for bin_ in bin_stream if len(bin_) == 8)

@utils.raise_warning(__warning_msg)
def encrypt_caesar_cypher(msg: str, shift: int=3, seed: str=string.ascii_lowercase) -> str:
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
    - Characters in `msg` that are not contained in `seed` escape encryption
    - The seed dictates language support
    - The ROT13 cypher is a special case of the caesar cypher (set `shift=13`)
    - A slightly stronger cypher can be obtained by using a shuffled `seed` with
    `math.factorial(26) * len(msg)` possible key combinations
    - This cypher's weakness is proportional to `len(msg)`, i.e. longer messages 
    are easier to break (the unicity distance of English equals 27.6 letters of
    cypher text for a simple substitution using a mixed alphabet as seed)
    - This method is also called simple substitution cypher if the seed is shuffled

    References
    ----------
    - <https://en.wikipedia.org/wiki/Caesar_cipher>
    - <https://en.wikipedia.org/wiki/Substitution_cipher>
    """
    return msg.translate(str.maketrans(seed, ''.join((seed[shift%len(seed):], seed[:shift%len(seed)]))))

def decrypt_caesar_cypher(cypher: str, shift: int=3, seed: str=string.ascii_lowercase) -> str:
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
    - There is no restriction on the type of characters, so this encryption method
    provides international language support
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
    msg = [''] * num_of_col
    col, row = 0, 0
    for char in cypher:
        msg[col] += char
        col += 1
        if (col == num_of_col) or (col == num_of_col - 1 and row >= key - ((num_of_col * key) - len(cypher))):
            col = 0
            row += 1
    return ''.join(msg)

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
    - Using the default seed (`len(seed)=100`), there are `key1 * key2 = 100 * 100 = 10000`
    key combinations to crack this cypher
    - The seed dictates language support
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

def __validate_vigenere_key(key: str, seed: str=string.ascii_lowercase):
    if not all(char in seed for char in key):
        err_msg = f"{key=} characters are not a subset of {seed=}"
        logger.error(err_msg)
        raise KeyError(err_msg)

@utils.raise_warning(__warning_msg)
def encrypt_vigenere_cypher(msg: str, key: str, seed: str=string.ascii_lowercase) -> str:
    """
    Encrypt a message using the vigenere cypher. All characters in `msg` and `key`
    should be limited to the `seed` set. IMPORTANT: Any character in `msg` that's
    not in `seed` will be skipped during the encryption process. Use `string.printable`
    as a seed to extend the scope of encryptionable characters in `msg` for English
    messages.

    Example
    -------
    ```
    >>> import string
    >>> from random import shuffle
    >>> from lolicon.compsci import cryptography as crypto
    >>> # generate random key from ASCII character set
    >>> key = list(string.printable)
    >>> shuffle(key)
    >>> key = ''.join(key)
    >>> msg = 'Hello, World!'
    >>> cypher = crypto.encrypt_vigenere_cypher(msg, key, string.printable)
    >>> print(msg == crypto.decrypt_vigenere_cypher(cypher, key, string.printable))
    True
    ```

    Suppose your key is `CLOCK` and your message `HELLO` with your seed set as
    `string.ascii_uppercase`. Then this function's map can be explained by the
    table below:
    ```
                                  2
                    1     0       3     4
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
          -----------------------------------------------------
        A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
    0,3 C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
        D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
        F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
        G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
        H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
        I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
        J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
      4 K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
      1 L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
        M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
        N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
      2 O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
        P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
        Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
        R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
      2 S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
        T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
        U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
        V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
        W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
        X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
        Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
        Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
    ```

    Enumerating the key characters along the left-most column we get
    ```
    0 1 2 3 4 # index
    H E L L O # msg
    C L O C K # key
    J P Z N Y # cypher
    ```

    Notes
    -----
    - Because it uses more than one set of substitutions, it is also called a
    polyaplhabetic substitution cypher
    - Longer keys enhance the encryption strength
    - The vigenere cypher is invulnerable to dictionary word pattern attacks
    - There are `len(key)^len(seed)` possible combinations to crack the cypher
    by using a brute force attack
    - Nevertheless, this cypher can still be broken with a combination of an
    Kasiski examination and a frequency analysis
    
    One-Time Pad Cypher
    -------------------
    This cypher is considered secure if and only if three conditions are met:
    1. The key is exactly as long as the message that is encrypted (ignoring
    punctuation and whitespace characters)
    2. The key is made up of truly random symbols (created with non-pseudo random
    generators)
    3. The key is only used once, and never used again for any other message
    
    If all this is true, the vigenere cypher promotes to the cryptographically
    secure one-time pad cypher (OTP).
    """    
    cypher = []
    offset = 0
    __validate_vigenere_key(key, seed)
    encrypt = lambda index: (seed.find(msg[index]) + seed.find(key[(index - offset) % len(key)])) % len(seed)

    for index in range(len(msg)):
        if msg[index] in seed:
            cypher.append(seed[encrypt(index)])
        else:
            cypher.append(msg[index])
            offset += 1

    return ''.join(cypher)

def decrypt_vigenere_cypher(cypher: str, key: str, seed: str=string.ascii_lowercase) -> str:
    """
    Decrypt a message using the vigenere cypher. Note that you need both, the key
    and seed, to decypher a message.
    """
    offset = 0
    msg = []
    __validate_vigenere_key(key, seed)
    decrypt = lambda index: (seed.find(cypher[index]) - seed.find(key[(index - offset) % len(key)])) % len(seed)

    for index in range(len(cypher)):
        if cypher[index] in seed:
            msg.append(seed[decrypt(index)])
        else:
            msg.append(cypher[index])
            offset += 1

    return ''.join(msg)
