#!/usr/bin/env python3

from __future__ import annotations

from functools import lru_cache

import math

def dec2bin(dec: int, padding: int=8) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    binary representation, i.e. a base-2 number system. Adjust `padding` to fill
    the binary number string with zeros (set to one byte by default).
    """
    bin_ = []
    while dec != 0:
        dec, r = divmod(dec, 2)
        bin_.append(str(r))
    return ''.join(reversed(bin_)).rjust(padding, '0')


def bin2dec(bin_: str) -> int:
    """
    Suppose that `bin_` is a valid binary number. Convert this number into its
    decimal representation.
    """
    return int(sum(map(lambda i: int(bin_[::-1][i]) * math.pow(2, i), range(len(bin_)))))

@lru_cache
def dec2base(dec: int, base: int) -> str:
    """
    Suppose that `dec` is an unsigned integer, and `base` an integer greater than
    or equal to 2. Translate `dec` into a radix-base representation.
    """
    r = int(dec % base)
    char_pos = lambda i: '0123456789ABCDEF'[i]
    return char_pos(r) if (dec - r) == 0 else dec2base((dec - r) / base, base) + char_pos(r)

def base2dec(num: str, base: int) -> int:
    """
    Suppose that `num` is a radix-based number. Translate `num` into its decimal
    number representation, i.e. a base-10 number system.
    """
    int_val = lambda c: '0123456789ABCDEF'.index(c)
    return sum((int_val(c) * math.pow(base, i) for i, c in enumerate(num[::-1])))

def dec2oct(dec: int) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    octal representation, i.e. a base-8 number system.
    """
    return dec2base(dec, 8)

def oct2dec(oct_: int) -> str:
    """
    Suppose that `oct_` is a valid octal number. Convert this number into its
    decimal representation.
    """
    return base2dec(oct_, 8)

def dec2hex(dec: int) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    hexadecimal representation, i.e. a base-16 number system.
    """
    return dec2base(dec, 16)

def hex2dec(hex_: str) -> int:
    """
    Suppose that `hex_` is a valid hexadecimal number. Convert this number into
    its decimal representation.
    """
    return base2dec(hex_.upper(), 16)
