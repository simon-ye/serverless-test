import unittest
from src.lib import common

class CommonTest(unittest.TestCase):
    def test_debug(self):
        common.debug("This is test for debug")