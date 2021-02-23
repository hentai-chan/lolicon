#!/usr/bin/env python3

import functools

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

@functools.lru_cache
def factorial(n: int) -> int:
    """
    Implements the recurrence definition of the factorial function: `n! = n(n-1)!`.
    """
    if n < 0:
        raise ValueError()
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def euler(n: int) -> float:
    """
    Uses the series definition to find an approximation of Euler's number.

    Note
    ----
    It takes `100` terms for this function to pass its unit test, i.e. to be equal
    when rounded to 7 decimal places.

    ```
    >>> from lolicon import mathematics
    >>> mathematics.euler(n=100)
    2.7182818284590455
    >>> # compare:
    >>> import lolicon.constants as const
    >>> const.EULER
    2.718281828459045
    ```
    """
    return sum(map(lambda k: 1**k / factorial(k), range(n)))

def pi(n: int) -> float:
    """
    Uses the Leibniz series definition to find an approximation of pi.

    Note
    ----
    It takes `1_000_000` terms for this function to pass its unit test,
    i.e. to be equal when rounded to 5 decimal places.

    ```
    >>> from lolicon import mathematics
    >>> mathematics.pi(n=1_000_000)
    3.1415916535897743
    >>> # compare:
    >>> import lolicon.constants as const
    >>> const.PI
    3.141592653589793
    ```
    """
    return 4 * sum(map(lambda k: (-1)**k / (2*k + 1), range(n)))
