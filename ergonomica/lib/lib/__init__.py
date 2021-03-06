#!/usr/bin/python
# -*- coding: utf-8 -*-

# these are the variable standards in other files (called inside functions)
# pylint: disable=invalid-name

"""
[lib/lib/__init__.py]

This module loads all commands from ergonomica.lib/lib into the 'verbs'
dictionary for running.
"""

import sys
from os import listdir, path
from ergonomica.lib.util.setup import setup

PACKAGES_PATH = path.join(path.expanduser("~"), ".ergo", "packages")

sys.path[0:0] = [PACKAGES_PATH]
sys.path[0:0] = [path.dirname(__file__)]

# load all commands from commands folder
try:
    commands = [x[:-3] for x in listdir(path.dirname(__file__)) +
                listdir(PACKAGES_PATH) if
                x.endswith(".py") and x != "__init__.py"]

except OSError:
    setup()
    print("Please restart ergonomica.")
    raise SystemExit

# namespace to hold functions
ns = {}

for item in commands:
    try:
        module = __import__(item, locals(), globals())
    except Exception as e:
        print(e)
    ns.update(module.exports)


del sys.path[0]
