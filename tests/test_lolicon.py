import unittest

import lolicon

class TestLolicon(unittest.TestCase):
    """
    Test unit test integration with GitHub Actions.
    """
    def test_hello(self):
        self.assertEqual(lolicon.hello(), "Hello, World!")