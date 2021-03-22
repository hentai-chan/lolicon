#!/usr/bin/env python3

import sys

__version__ = "0.0.6a"
package_name = "lolicon"
python_major = "3"
python_minor = "7"

try:
    assert sys.version_info >= (int(python_major), int(python_minor))
except AssertionError:
    raise RuntimeError(f"\033[91m{package_name.capitalize()} requires Python {python_major}.{python_minor}+ (You have Python {sys.version})\033[0m")
