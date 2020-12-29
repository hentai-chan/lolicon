#!/usr/bin/env python3

from __future__ import annotations

import json
from importlib.resources import path as resource_path
from typing import List


def load_resource(resource: str, package: str) -> List[dict]:
     with resource_path(resource, package) as resource_handler:
         with open(resource_handler, mode='r', encoding='utf-8') as file_handler:
             return json.load(file_handler)
