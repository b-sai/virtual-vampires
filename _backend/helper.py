from cgi import test
from backend_scripts.converters.english import EnglishConverter
from backend_scripts.converters.swahili import SwahiliConverter
import pandas as pd
from backend_scripts.utils import exc_to_dict


def swahili_to_english(feats):
    """
    Get last item of feats, convert to english, return
    """
    df = pd.read_csv("data/dict.tsv", sep="\t", header=None)
    sw_word = feats.split("+")[-1]
    en_translated = df[df[0] == sw_word][1].values[0]
    return feats[:feats.rindex("+")] + "+" + en_translated



def test_demo(out_file="data/submission_out.txt"):
    sentences = []
    results = []
    with open("data/submission.txt", "r") as f:
        for line in f:
            sentences.append(line.strip())
    
    past_tense_exc = exc_to_dict("data/past_tense_exceptions.csv")
    past_part_exc = exc_to_dict("data/irregular_verbs_past_participle.csv")

    english = EnglishConverter(past_tense_exc, past_part_exc)
    swahili = SwahiliConverter()
    
    for sentence in sentences:
        english_sent = english.generate_sentence(swahili_to_english(sentence))
        swahili_sent = swahili.generate_sentence(sentence)
        with open(out_file, "a") as f:
            f.write(f"{sentence}\t{english_sent:}\t{swahili_sent}\n")
    
    
test_demo()

