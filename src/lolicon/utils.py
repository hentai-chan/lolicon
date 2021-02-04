#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
import sqlite3
from contextlib import closing
from importlib.resources import path as resource_path
from typing import Iterable, List

import pint
from colorama import Fore, Style

UREG = pint.UnitRegistry()


def load_resource(resource: str, package: str) -> List[dict]:
    with resource_path(resource, package) as resource_handler:
        with open(resource_handler, mode='r', encoding='utf-8') as file_handler:
            return json.load(file_handler)


def query_db(db: str, sql: str, *args, local_: bool=False) -> List:
    with resource_path('src.lolicon.data' if local_ else 'lolicon.data', db) as resource_handler:
        with closing(sqlite3.connect(resource_handler)) as connection:
            with closing(connection.cursor()) as cursor:
                return cursor.execute(sql, *args).fetchall()


def raise_on_none(variable: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if func(*args, **kwargs) is None:
                    raise ValueError(
                        f"{Fore.RED}{variable} is None{Style.RESET_ALL}")
                return func(*args, **kwargs)
            except TypeError:
                raise ValueError(
                    f"{Fore.RED}{variable} is None{Style.RESET_ALL}")
        return wrapper
    return decorator


@raise_on_none('string')
def str_to_bool(string: str) -> bool:
    """
    Convert string to boolean if string is not `None`, else raise `ValueError`.
    """
    return (string.capitalize() == 'True' or string.capitalize() == 'Yes') if string is not None else None
