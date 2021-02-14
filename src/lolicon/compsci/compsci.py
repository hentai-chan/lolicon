#!/usr/bin/env python3

from __future__ import annotations

import math

def dec2bin(dec: int) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    binary representation.
    """
    bin_ = []
    while dec != 0:
        dec, r = divmod(dec, 2)
        bin_.append(str(r))
    return ''.join(reversed(bin_))


def bin2dec(bin_: str) -> int:
    """
    Suppose that `bin` is a valid binary number. Convert this number into its
    decimal representation.
    """
    return sum(map(lambda i: int(bin_[::-1][i]) * math.pow(2, i), range(len(bin_))))
