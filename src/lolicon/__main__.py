#!/usr/bin/env python3

from .cli import cli
from .utils import logger

if __name__ == 'main':
    try:
        cli()
    except KeyboardInterrupt:
        logger.info('Disrupted CLI execution.')
