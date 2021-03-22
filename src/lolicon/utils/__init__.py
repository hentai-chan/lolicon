#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
import logging
import os
import platform
import sqlite3
import warnings
from collections import namedtuple
from contextlib import closing
from importlib.resources import path as resource_path
from pathlib import Path
from types import FrameType
from typing import List

import click
import pint
from colorama import Fore, Style
from rich.console import Console
from rich.table import Table

from ..__init__ import package_name
from .requesthandler import RequestHandler

UREG = pint.UnitRegistry()
CONSOLE = Console()

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

def debug(msg: str, frame: FrameType) -> None:
    """
    Helper function for slightly better print debugging. Prints the current line
    of invocation, a custom `msg` and the source file name as color-formatted string.
    Set `frame` to `inspect.currentframe()` when you invoke this function.

    Example
    -------
    ```
    import inspect

    # some code
    debug('Validate incoming data stream.', frame=inspect.currentframe())
    # ...
    debug('Enter recursive function.', frame=inspect.currentframe())
    ```

    Note
    ----
    Consider using an IDE with a debugger whenever possible.
    """
    print(f"\033[93m[{str(frame.f_lineno).zfill(4)}]\033[0m\t\033[92m{msg}\033[0m (in {Path(frame.f_code.co_filename).name}).")

#endregion

#region log utilities

def log_file_path(target_dir: str) -> Path:
    """
    Make a `target_dir` folder in the user's home directory, create a log
    file (if there is none, else use the existsing one) and return its path.
    """
    directory = Path(os.path.expandvars('%LOCALAPPDATA%')) if platform.system() == 'Windows' else Path().home()
    directory = directory.joinpath(f".{target_dir}")
    directory.mkdir(parents=True, exist_ok=True)
    directory.mkdir(parents=True, exist_ok=True)
    log_file = directory.joinpath(f"{target_dir}.log")
    log_file.touch(exist_ok=True)
    return log_file

LOGFILEPATH = log_file_path(target_dir=package_name)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(lineno)d::%(name)s::%(message)s', datefmt='%d-%b-%y %H:%M:%S')
file_handler = logging.FileHandler(LOGFILEPATH)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_log():
    """
    Read color-formatted log file content from the lolicon module.
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

        table = Table(title="Log File Content")
        table.add_column('Timestamp', style='cyan')
        table.add_column('Level Name')
        table.add_column('File Name')
        table.add_column('Line Number')
        table.add_column('Message', style='green')

        parse = lambda line: line.strip('\n').split('::')
        Entry = namedtuple('Entry', 'timestamp levelname lineno name message')
        
        for entry in [Entry(parse(line)[0], parse(line)[1], parse(line)[2], parse(line)[3], parse(line)[4]) for line in log]:
            table.add_row(entry.timestamp, f"[bold {color_map[entry.levelname]}]{entry.levelname}", entry.name, entry.lineno, entry.message)
        
        CONSOLE.print(table)

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
    log_msg = f"{variable} is None"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if func(*args, **kwargs) is None:
                    logger.error(log_msg)
                    raise ValueError(f"{Fore.RED}{log_msg}{Style.RESET_ALL}")
                return func(*args, **kwargs)
            except TypeError:
                logger.error(log_msg, exc_info=True)
                raise ValueError(f"{Fore.RED}{log_msg}{Style.RESET_ALL}")
        return wrapper
    return decorator

def raise_warning(msg: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.warning(msg)
            warnings.warn(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}", stacklevel=3)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@raise_on_none('string_')
def str_to_bool(string_: str) -> bool:
    """
    Convert string to boolean if string is not `None`, else raise `ValueError`.
    """
    return (string_.capitalize() == 'True' or string_.capitalize() == 'Yes') if string_ is not None else None
