#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/ergo_python.py]

Defines the "python" command.
"""

import sys
from ptpython.repl import embed

Symbol = str          # A Scheme Symbol is implemented as a Python str
List   = list         # A Scheme List is implemented as a Python list
Number = (int, float) # A Scheme Number is implemented as a Python int or float

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    import os
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

def main(argc):
    """python: Python ergonomica integration.

    Usage:
       python [(--file FILE | STRING)]
    """
    if argc.args['--file']:
        # pylint seems to think execfile isn't defined
        execfile(argc.args['FILE']) # pylint: disable=undefined-variable
        return

    elif argc.args['STRING']:
        globals().update(argc.ns)
        globals()['stdin'] = argc.stdin
        # ergonomica is a shell
        # pylint: disable=eval-used
        return eval(argc.args['STRING'], globals())

    try:
        temp_space = globals()

        # export ergonomica variables
        for item in argc.ns:
            if not callable(argc.ns[item]):
                temp_space[item] = argc.ns[item]

        temp_space.update({"exit":sys.exit})
        temp_space.update({"quit":sys.exit})
        temp_space.update(argc.env.namespace)

        _vi_mode = False
        if argc.env.EDITOR in ["vi", "vim"]:
            _vi_mode = True

        embed(globals(), temp_space, vi_mode=_vi_mode)
    except SystemExit:
        for key in temp_space:
            if not callable(temp_space[key]):
                argc.ns[key] = temp_space[key]
        return
