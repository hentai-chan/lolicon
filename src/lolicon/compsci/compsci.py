#!/usr/bin/env python3

from __future__ import annotations

from math import pow

def dec2bin(dec: int) -> str:
    """
    Suppose that `dec` is an unsigned integer. Convert this number into its
    binary representation.
    """
    bin = []
    while dec != 0:
        dec, r = divmod(dec, 2)
        bin.append(str(r))
    return ''.join(reversed(bin))


def bin2dec(bin: str) -> int:
    """
    Suppose that `bin` is a valid binary number. Convert this number into its
    decimal representation.
    """
    return sum(map(lambda i: int(bin[i]) * pow(2, i), reversed(range(len(bin)))))