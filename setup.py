#!/usr/bin/env python
import re

from setuptools import setup

with open("lolicon/__init__.py", encoding='utf8') as file_handler:
    version = re.search(r'__version__ = "(.*?)"', file_handler.read()).group(1)

with open("requirements.txt", encoding='utf-8') as file_handler:
    packages = file_handler.read().splitlines()

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="lolicon",
    version=version,
    install_requires=packages,
)
