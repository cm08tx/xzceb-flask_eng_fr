"""Functions to test 'English to French' and 'French to English'"""

import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """Test English to French"""
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'guten tag')

class TestF2E(unittest.TestCase):
    """Translate French to English"""
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('bonjour'), 'guten tag')

unittest.main()
