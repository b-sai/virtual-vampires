from tense_converter import to_past, to_future, to_past_perfect, get_past_participle
import pandas as pd

def sentence_generator(feat_sent:str):
    
    feats = feat_sent.split("+")
    verb = feats[-1]
    feats = feats[:-1]
    
    result = ""
    
    for feat in feats:
        if feat == 'PAST':
            result += " " + to_past(verb, pt_exc)
        elif feat == 'FUT':
            result += " " + to_future(verb)
        elif feat == 'PERF':
            result += " " + to_past_perfect(verb, p_part_exc)
        elif feat == "1s":
            result += " I"
        elif feat == "2s":
            result += " you"
        elif feat == "3s":
            result += " he"
        elif feat == "1p":
            result += " we"
        elif feat == "2p":
            result += " you"
        elif feat == "3p":
            result += " they"
        elif feat == "NEG":
            result += " not"

    return result


pt_exc = pd.read_csv("data/past_tense_exceptions.csv")
p_part_exc = pd.read_csv("data/irregular_verbs_past_participle.csv")


def df_to_dict(df):
    return dict(zip(df.iloc[:, 0], df.iloc[:, 1]))


pt_exc = df_to_dict(pt_exc)
p_part_exc = df_to_dict(p_part_exc)

res = sentence_generator("1s+PAST+jump")
print(res)
res = sentence_generator("NEG+2s+PERF+tell")
print(res)


