#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
import logging
import platform
import sqlite3
import warnings
from contextlib import closing
from importlib.resources import path as resource_path
from os.path import expandvars
from pathlib import Path
from typing import List

import pint
from colorama import Fore, Style

UREG = pint.UnitRegistry()


def _hidden_module_path(target_dir: str) -> Path:
    """
    Return the base config path for this module.
    """
    directory = Path(expandvars('%LOCALAPPDATA%')) if platform.system() == 'Windows' else Path('/etc')
    directory = directory.joinpath(target_dir)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(lineno)d::%(name)s::%(message)s', datefmt='%d-%b-%y %H:%M:%S')
file_handler = logging.FileHandler(_hidden_module_path(target_dir='.lolicon').joinpath('lolicon.log'))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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

def raise_warning(msg: str, surpress_warning: bool=False):
    """
    Warning utility method. To be called at the top of a function block to indicate
    cryptographically insecure methods or depreaction candidates. Enable `surpress_warning`
    to ignore warning messages in unit tests.
    """
    if not surpress_warning:
        warnings.warn(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}", stacklevel=3)

@raise_on_none('string')
def str_to_bool(string: str) -> bool:
    """
    Convert string to boolean if string is not `None`, else raise `ValueError`.
    """
    return (string.capitalize() == 'True' or string.capitalize() == 'Yes') if string is not None else None
