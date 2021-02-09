#!/usr/bin/env python3

import string

from .. import utils
from ..utils import logger

__warning_msg = "You're using an cryptographically insecure method."

def hello_world(surpress_warning: bool=False) -> str:
    utils.raise_warning(__warning_msg, surpress_warning)
    logger.info('test logger!')
    return 'Hello, World!'