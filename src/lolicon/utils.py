#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
import logging
import os
import platform
import sqlite3
import warnings
from contextlib import closing
from importlib.resources import path as resource_path
from pathlib import Path
from typing import List

import pint
import click
from colorama import Fore, Style

from .__init__ import package_name

UREG = pint.UnitRegistry()

#region terminal formatting

def print_on_success(message: str, verbose: bool=True) -> None:
    """
    Print a formatted success message if verbose is enabled.
    """
    if verbose:
        click.secho(f"{Style.BRIGHT}{Fore.GREEN}{'[  OK  ]'.ljust(12, ' ')}{Style.RESET_ALL}{message}")

def print_on_warning(message: str, verbose: bool=True) -> None:
    """
    Print a formatted warning message if verbose is enabled.
    """
    if verbose:
        click.secho(f"{Fore.YELLOW}{'[ WARNING ]'.ljust(12, ' ')}{Style.RESET_ALL}{message}")

def print_on_error(message: str, verbose: bool=True) -> None:
    """
    Print a formatted error message if verbose is enabled.
    """
    if verbose:
        click.secho(f"{Style.BRIGHT}{Fore.RED}{'[ ERROR ]'.ljust(12, ' ')}{Style.RESET_ALL}{message}", err=True)

#endregion

#region log utilities

def _hidden_module_path(target_dir: str) -> Path:
    """
    Return the base config path for this module.
    """
    directory = Path(os.path.expandvars('%LOCALAPPDATA%')) if platform.system() == 'Windows' else Path('/var/log')
    directory = directory.joinpath(target_dir)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

LOGFILEPATH = _hidden_module_path(target_dir=f".{package_name}").joinpath(f"{package_name}.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(lineno)d::%(name)s::%(message)s', datefmt='%d-%b-%y %H:%M:%S')
file_handler = logging.FileHandler(LOGFILEPATH)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_log():
    """
    Read color-formatted log file content from the speedtest module.
    """
    color_map = {
        'NOTSET': 'white',
        'DEBUG': 'bright_blue',
        'INFO': 'yellow',
        'WARNING': 'bright_magenta',
        'ERROR': 'red',
        'CRITICAL': 'bright_red'
    }
    with open(LOGFILEPATH, mode='r', encoding='utf-8') as file_handler:
        log = file_handler.readlines()

        if not log:
            print_on_warning("Operation suspended: log file is empty.")
            return

        click.secho("\nLOG FILE CONTENT\n", fg='bright_magenta')

        for line in log:
            entry = line.strip('\n').split('::')
            timestamp, levelname, lineno, name, message = entry[0], entry[1], entry[2], entry[3], entry[4]
            click.secho(f"[{timestamp}] ", fg='cyan', nl=False)
            click.secho(f"{levelname}\t", fg=color_map[levelname], blink=(levelname=='CRITICAL'), nl=False)
            click.secho(message, fg='bright_green', nl=False)
            click.secho(f" ({name}@{lineno})")

#endregion

#region i/o operations

def load_resource(resource: str, package: str) -> List[dict]:
    with resource_path(resource, package) as resource_handler:
        with open(resource_handler, mode='r', encoding='utf-8') as file_handler:
            return json.load(file_handler)

def query_db(db: str, sql: str, *args, local_: bool=False) -> List:
    with resource_path('src.lolicon.data' if local_ else 'lolicon.data', db) as resource_handler:
        with closing(sqlite3.connect(resource_handler)) as connection:
            with closing(connection.cursor()) as cursor:
                return cursor.execute(sql, *args).fetchall()

#endregion

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

def raise_warning(msg: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}", stacklevel=3)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@raise_on_none('string')
def str_to_bool(string: str) -> bool:
    """
    Convert string to boolean if string is not `None`, else raise `ValueError`.
    """
    return (string.capitalize() == 'True' or string.capitalize() == 'Yes') if string is not None else None
