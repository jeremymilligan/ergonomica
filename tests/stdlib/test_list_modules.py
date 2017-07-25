"""
[tests/stdlib/test_list_modules.py]

Test the list_modules command.
"""

import unittest
import os

from ergonomica.ergo import ergo


class TestListModules(unittest.TestCase):
    """Tests the `list_modules` command."""

    def test_list_modules(self):
        """
        Test the list_modules function.
        """
        
        self.assertEqual(ergo('list_modules'), ["__init__", "epm"])