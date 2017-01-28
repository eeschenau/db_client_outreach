#!/usr/bin/env python
# ------------
# Esther Schenau
# Start Date: 28Jan2016
# Database Interface for user outreach. Function tests.
# ------------
import unittest
from db_func import *

class MyTest (unittest.TestCase):
    def test(self):
        self.assertEqual(function(inputval, expected_value)
