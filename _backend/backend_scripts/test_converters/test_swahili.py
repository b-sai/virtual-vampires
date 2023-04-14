import unittest
from _backend.backend_scripts.converters.swahili import SwahiliConverter
import pandas as pd
from _backend.backend_scripts.utils import exc_to_dict

class TestSwahili(unittest.TestCase):
    def test_demo(self):
        sentences = []
        with open("data/testdist.tsv", "r") as f:
            for line in f:
                sentences.append(line.strip().split("\t"))
        
        #past_tense_exc = exc_to_dict("data/past_tense_exceptions.csv")
        irregular_exc = exc_to_dict("data/irregular_verbs_swahili.csv")
        
        swahili = SwahiliConverter(irregular_exc)
        
        for feats,english_sent, swahili_sent in sentences:
            res = swahili.generate_sentence(feats)
            self.assertEqual(res, swahili_sent)

if __name__ == '__main__':
    unittest.main()
