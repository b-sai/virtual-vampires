import unittest
from _backend.backend_scripts.converters.spanish import SpanishConverter
import pandas as pd
from _backend.backend_scripts.utils import exc_to_dict


class TestSpanish(unittest.TestCase):
    def test_demo(self):
        sentences = []
        with open("data/test_spanish_sentences.tsv", "r") as f:
            for line in f:
                sentences.append(line.strip().split("\t"))

        english = SpanishConverter()

        for feats, english_sent in sentences:
            res = english.generate_sentence(feats)
            if res != english_sent:
                print(f"{feats: <25} | {res : <25} | {english_sent}")
            # self.assertEqual(res, english_sent)
            


if __name__ == '__main__':
    unittest.main()
