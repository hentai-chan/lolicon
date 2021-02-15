#!/usr/bin/env python3

def gcd(a: int, b: int) -> int:
    """
    Return the greatest common denominator of `x` and `y` by using Euclid's GCD algorithm.

    Example
    -------
    >>> from lolicon.mathematics import gcd
    >>> gcd(24, 30)
    >>> 6
    """
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a: int, m: int) -> int or None:
    """
    The modular inverse of two numbers `a` and `m` is defined by the equation
    `(a * i) % m = 1`. The value only exists if `a` and `m` are relatively prime.
    If that's not the case, this function will return `None` instead.

    Example
    -------
    >>> from lolicon.mathematics import mod_inverse
    >>> mod_inverse(5, 7)
    >>> 3

    Note
    ----
    - This function uses Euclid's Extended Algorithm to find the modular inverse.
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
