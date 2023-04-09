from .converter import TenseConverter
from SwahiliDictionary import pronouns, tense, tense_negations, pronouns_negation

class SwahiliConverter(TenseConverter):

    def __init__(self):
        super().__init__()
        # add any exception files here
    def to_past(self, verb, is_neg, sp):
        if is_neg:
            return pronouns_negation[sp] + Negation_tense["Past"] + verb[2:]
        else:
            return pronouns[sp] + tense["Past"] + verb[2:]
    def to_present(self,verb, is_neg, sp):
        if is_neg:
            if verb[-1] == "a":
                return (pronouns_negation[sp] + verb[2:-1] + "i")
            else:
                return (pronouns_negation[sp] +  verb[2:])
        else:
            return pronouns[sp]  + tense["Present"] + verb[2:]
    def to_future(self, verb, is_neg, sp):
        if is_neg:
            return pronouns_negation[sp] + Negation_tense["Future"] + verb[2:]
        else:
            return pronouns[sp] + tense["Future"] + verb[2:]

    def to_past_perfect(self, verb, is_neg, sp):
        return "Not Done Yet"
    
    def to_imperfect(self, verb):
        return verb[2:]

    def method_dispatcher(self,method_name):
        methods = {"PAST":self.to_past, "PRES":self.to_present, "FUT":self.to_future, 
                    "PERF":self.to_past_perfect, "IMP":self.to_imperfect}
        return methods[method_name]
    def generate_sentence(self, features):
        feats = features.split("+")
        verb = feats[-1]
        #####finish this tomorrow####
        if feats[0] == "NEG":
            sp = feats[1]
            tense = feats[2]
            is_neg = True
        else:
            sp = feats[0]
            tense = feats[1]
            is_neg = False
        return self.method_dispatcher(tense)(verb, is_neg, sp)
