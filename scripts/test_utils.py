import unittest
from scripts.utils import is_valid_url


class TestUtils(unittest.TestCase):

    def test_is_valid_url(self):
        self.assertTrue(is_valid_url("http://www.sieve.com.br"))
        self.assertTrue(is_valid_url("https://www.sieve.com.br"))
        self.assertTrue(is_valid_url("https://www.sieve.com"))
        self.assertTrue(is_valid_url("http://www.sieve.com"))
        self.assertTrue(is_valid_url("https://sieve.com"))
        self.assertTrue(is_valid_url("http://sieve.com"))

    def test_is_valid_url_fail(self):
        self.assertFalse(is_valid_url("ftp://sieve.com"))
        self.assertFalse(is_valid_url("http://sieve"))
        self.assertFalse(is_valid_url("http://"))
