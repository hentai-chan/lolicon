#!/usr/bin/env python3

def gcd(x: int, y: int) -> int:
    """
    Return the greatest common denominator of `x` and `y`.
    """
    while y:
        x, y = y, x % y
    return x