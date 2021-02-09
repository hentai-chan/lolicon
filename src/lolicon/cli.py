#!/usr/bin/env python3

import click
from click import style

try:
    import pretty_errors
except ImportError:
    pass

from . import utils
from .__init__ import __version__, package_name

CONTEXT_SETTINGS = dict(max_content_width=120)

@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS, help=style("A modern CLI template for python scripts.", fg='bright_magenta'))
@click.version_option(version=__version__, prog_name=package_name, help=style("Show the version and exit.", fg='yellow'))
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)

@cli.command(help=style("Perform log file operations.", fg='bright_green'), context_settings=CONTEXT_SETTINGS)
@click.option('--read', is_flag=True, default=False, help=style("Read the log file.", fg='yellow'))
@click.option('--reset', is_flag=True, default=False, help=style("Reset all log file entries", fg='yellow'))
@click.option('--path', is_flag=True, default=False, help=style("Get the log file path.", fg='yellow'))
def log(read, reset, path):
    if read:
        utils.read_log()
        return

    if reset:
        open(utils.LOGFILEPATH, mode='w', encoding='utf-8').close()
        return

    if path:
        click.echo(utils.LOGFILEPATH)
        return
