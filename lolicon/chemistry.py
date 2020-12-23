#!/usr/bin/env python3

import json

class PSE(object):
    @staticmethod
    def table(index):
        # NOTE: import pse.json as resource path in release version
        with open('lolicon/data/pse.json', mode='r', encoding='utf-8') as file_handler:
            reader = json.load(file_handler)
            return reader[index]