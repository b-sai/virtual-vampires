from .converter import TenseConverter


def sentence_generator(feat_sent: str,  converter: TenseConverter):

    feats = feat_sent.split("+")

    verb = feats[-1]

    is_neg = False
    result = ""
    if "IMP" in feats:
        return verb

    for feat in feats:

        if feat == 'PAST':
            result += " " + converter.to_past(verb, is_neg)
        elif feat == 'FUT':
            result += " " + converter.to_future(verb, is_neg)
        elif feat == 'PERF':
            result += " " + converter.to_past_perfect(verb, is_neg)
        elif feat == 'PRES':
            result += " " + converter.to_present(verb, is_neg)

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

