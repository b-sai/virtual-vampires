from .converter import TenseConverter


class SpanishConverter(TenseConverter):

    def __init__(self) -> None:
        super().__init__()
        # add any exception files here

    def to_past(self, verb, is_neg):
        return "yo"

    def to_present(self, verb, is_neg):
        return ""

    def to_future(self, verb, is_neg):
        return ""

    def to_past_perfect(self, verb, is_neg):
        return ""

    def to_imperfect(self, verb):
        return ""
    
    def to_s(self, verb, feat):
        if feat == "1s":
            return "yo"
        elif feat == "2s":
            return "tu"
        elif feat == "3s":
            return "el"
    
    def generate_sentence(self, features):
        feats = features.split("+")

        verb = feats[-1]

        is_neg = False
        result = ""
        if "IMP" in feats:
            return verb

        is_plural = False

        sp = ""

        for feat in feats:

            if feat == 'PAST':
                result += " " + self.to_past(verb, is_neg)
            elif feat == 'FUT':
                result += " " + self.to_future(verb, is_neg)
            elif feat == 'PERF':
                result += " " + self.to_past_perfect(verb, is_neg)
            elif feat == 'PRES':
                result += " " + self.to_present(verb, is_neg)

            elif feat in ["1s", "2s", "3s"]:
                result += self.to_s(verb, feat)
                sp = feat
            elif feat == "1p":
                result += "nosotros/nosotras"
                sp = feat
            elif feat == "2p":
                result += "ustedes"
                sp = feat
            elif feat == "3p":
                result += "ellos/ellas"
                sp = feat
            elif feat == "NEG":
                is_neg = True

        return result
