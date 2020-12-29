#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
from importlib.resources import path as resource_path
from typing import List

from colorama import Fore, Style
import pint

UNIT = pint.UnitRegistry()


def load_resource(resource: str, package: str) -> List[dict]:
     with resource_path(resource, package) as resource_handler:
         with open(resource_handler, mode='r', encoding='utf-8') as file_handler:
             return json.load(file_handler)

def raise_on_none(variable: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    if func(*args, **kwargs) is None:
                        raise ValueError(f"{Fore.RED}{variable} is None{Style.RESET_ALL}")
                    return func(*args, **kwargs)
                except TypeError:
                    raise ValueError(f"{Fore.RED}{variable} is None{Style.RESET_ALL}")
            return wrapper
        return decorator
