#!/usr/bin/env python3

from __future__ import annotations

import math

def dec2bin(dec: int, pad_zero: int=8) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    binary representation. Adjust `pad_zero` to fill the binary number string
    with zeros (set to one byte by default).
    """
    bin_ = []
    while dec != 0:
        dec, r = divmod(dec, 2)
        bin_.append(str(r))
    return ''.join(reversed(bin_)).rjust(pad_zero, '0')


def bin2dec(bin_: str) -> int:
    """
    Suppose that `bin` is a valid binary number. Convert this number into its
    decimal representation.
    """
    return int(sum(map(lambda i: int(bin_[::-1][i]) * math.pow(2, i), range(len(bin_)))))
