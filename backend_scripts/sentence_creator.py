from tense_converter import to_past, to_future, to_past_perfect, get_past_participle, to_present
import pandas as pd



def sentence_generator(feat_sent:str, verb:str, input_lang:str):
    
    feats = feat_sent.split("+")
    
    # tests cases have swahili verbs. 
    # using verb param, I can ignore the swahili verb and use the english verb instead
    # mainly used for testing correctness of the sentence generator
    
    if input_lang.lower() == "english":
        verb = feats[-1]
    
    #ignore the verb
    feats = feats[:-1]

    is_neg = False
    result = ""
    if "IMP" in feats:
        return verb
    
    for feat in feats:
        
        if feat == 'PAST':
            result += " " + to_past(verb, pt_exc, is_neg)
        elif feat == 'FUT':
            result += " " + to_future(verb, is_neg)
        elif feat == 'PERF':
            result += " " + to_past_perfect(verb, p_part_exc, is_neg)
        elif feat == 'PRES':
            result += " " + to_present(verb, is_neg)
            
        elif feat == "1s":
            result += "I"
        elif feat == "2s":
            result += "you"
        elif feat == "3s":
            result += "(s)he"
        elif feat == "1p":
            result += "we"
        elif feat == "2p":
            result += "you"
        elif feat == "3p":
            result += "they"
        elif feat == "NEG":
            is_neg = True

    return result


pt_exc = pd.read_csv("data/past_tense_exceptions.csv")
p_part_exc = pd.read_csv("data/irregular_verbs_past_participle.csv")


def df_to_dict(df):
    return dict(zip(df.iloc[:, 0], df.iloc[:, 1]))


pt_exc = df_to_dict(pt_exc)
p_part_exc = df_to_dict(p_part_exc)

res = sentence_generator("1s+PAST+jump",verb = None, input_lang="english")
res = sentence_generator("1p+PRES+kuishi", verb=None, input_lang="english")

df = pd.read_csv("data/dict.tsv", sep="\t", header=None, names=["Swahili", "English"])

def language_converter(input_lang, output_lang, word, df):
    return df[output_lang][df[input_lang] == word].values[0]

df = pd.read_csv("data/dict.tsv", sep="\t", header=None,
                 names=["Swahili", "English"])

line = "1p+PRES+kuishi"
feats= line
verb = feats.split("+")[-1]
verb = language_converter("Swahili", "English", verb, df)
print(feats, verb)
res = sentence_generator(feats, verb=verb, input_lang="swahili")
print(res)
print(f"{feats:<20} | {res:<20} ")



for line in open("data/testdist.tsv", "r"):
    line = line.strip()
    tokens = line.split("\t")
    feats, eng, swahili = tokens[0], tokens[1], tokens[2]
    verb = feats.split("+")[-1]
    verb = language_converter("Swahili", "English", verb, df)
    res = sentence_generator(feats, verb=verb, input_lang="swahili")
    print(f"{feats:<25} | {res:<25} | {eng:<25}| {res == eng:<25}")



