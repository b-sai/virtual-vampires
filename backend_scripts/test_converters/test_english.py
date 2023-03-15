import unittest
from backend_scripts.converters.english import EnglishConverter
from backend_scripts.converters.generate_sentence import sentence_generator
import pandas as pd


class TestEnglish(unittest.TestCase):
    
    def test_upper(self):
        
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
