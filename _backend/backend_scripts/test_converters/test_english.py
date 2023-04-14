import unittest
from _backend.backend_scripts.converters.english import EnglishConverter
import pandas as pd
from _backend.backend_scripts.utils import exc_to_dict

class TestEnglish(unittest.TestCase):
    def test_demo(self):
        sentences = []
        with open("data/test_english_sentences.tsv", "r") as f:
            for line in f:
                sentences.append(line.strip().split("\t"))
        
        past_tense_exc = exc_to_dict("data/past_tense_exceptions.csv")
        past_part_exc = exc_to_dict("data/irregular_verbs_past_participle.csv")

        english = EnglishConverter(past_tense_exc, past_part_exc)
        
        for feats,english_sent in sentences:
            res = english.generate_sentence(feats)
            self.assertEqual(res, english_sent)

if __name__ == '__main__':
    unittest.main()
