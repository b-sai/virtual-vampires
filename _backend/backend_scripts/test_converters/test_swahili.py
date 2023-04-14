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
        #past_part_exc = exc_to_dict("data/irregular_verbs_past_participle.csv")
        
        swahili = SwahiliConverter()
        
        for feats,english_sent, swahili_sent in sentences:
            feats2 = feats.split("+")
            verb = feats2[-1]
            if feats2[0] == "NEG":
                sp = feats2[1]
                tense = feats2[2]
                is_neg = True
            else:
                sp = feats2[0]
                tense = feats2[1]
                is_neg = False
            if (tense != "IMP"):
                res = swahili.generate_sentence(feats)
                self.assertEqual(res, swahili_sent)

if __name__ == '__main__':
    unittest.main()
