import unittest
import pandas as pd
from sentence_creator import sentence_generator, language_converter

class TestSentenceGenerator(unittest.TestCase):
    
    def test_sentence_generator(self):
        df = pd.read_csv("data/dict.tsv", sep="\t", header=None, names=["Swahili", "English"])
        for line in  open("data/testdist.tsv", "r"):
            line = line.strip()
            tokens = line.split("\t")
            feats, eng, swahili = tokens[0], tokens[1], tokens[2]
            verb = feats.split("+")[-1]
            language_converter("swahili", "english", verb, df)
            res = sentence_generator(feats, verb=verb, input_lang="swahili")
            self.TestCase.assertEqual(res, swahili)
