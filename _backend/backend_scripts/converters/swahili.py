from .converter import TenseConverter
from .SwahiliDictionary import pronouns, tense, tense_negations, pronouns_negation

class SwahiliConverter(TenseConverter):

    def __init__(self, irregular_verbs:dict = None):
        super().__init__()
        self.irregular_verbs = irregular_verbs
        # add any exception files here
    def to_past(self, verb, is_neg, sp):
        # if is_neg and verb[2:] == "la":
        #     return pronouns_negation[sp] + tense_negations["Past"] + verb
        if is_neg:
            return pronouns_negation[sp] + tense_negations["Past"] + verb[2:]
        elif verb[2:] in ["la", "fa", "ja"]:
            return pronouns[sp]  + tense["Past"] + verb
        else:
            return pronouns[sp]  + tense["Past"] + verb[2:]
    def to_present(self,verb, is_neg, sp):
        if is_neg:
            if verb[-1] == "a":
                return (pronouns_negation[sp] + verb[2:-1] + "i")
            else:
                return (pronouns_negation[sp] +  verb[2:])
        elif verb[2:] in ["la", "fa", "ja"]:
            return pronouns[sp]  + tense["Present"] + verb
        else:
            return pronouns[sp]  + tense["Present"] + verb[2:]
    def to_future(self, verb, is_neg, sp):
        if is_neg and verb[2:] in ["la", "fa", "ja"]:
            return pronouns_negation[sp] + tense_negations["Future"] + verb
        if is_neg:
            return pronouns_negation[sp] + tense_negations["Future"] + verb[2:]
        elif verb[2:] == "la":
            return pronouns[sp]  + tense["Future"] + verb
        else:
            return pronouns[sp]  + tense["Future"] + verb[2:]

    def to_past_perfect(self, verb, is_neg, sp):
    #confirm the rules with doctor scannel, have some doubts here regarding how singular and plural are trated
    #in past perfect negation    
        if is_neg and sp[1] != "s" and verb[2:] in ["la", "fa", "ja"]:
            return pronouns_negation[sp] + tense_negations["Perfect"] + verb
        if is_neg:
            return pronouns_negation[sp] + tense_negations["Perfect"] + verb[2:]
        elif verb[2:] == "la":
            return pronouns[sp]  + tense["Perfect"] + verb
        else:
            return pronouns[sp]  + tense["Perfect"] + verb[2:]
    
    # the imperative has been changed so that there is no conflict with the api since it randomly uses 1s person and 3rd person
    # which may not be valid with swahili
    def to_imperitive(self, verb, is_neg, sp):
        if(verb not in self.irregular_verbs and sp[1] == "s"):
            #how does the ["la", "fa", "ja"] conditional act in the case of plural?
            if verb[2:] in ["la", "fa", "ja"]:
                return verb
            else:
                return verb[2:]
        #think about 3rd person plural later
        elif(verb not in self.irregular_verbs and sp[1] == "p"):
            if verb[-1] == "a":
                return verb[2:-1] + "eni"
            else:
                return verb[2:] + "ni"
        elif(verb in self.irregular_verbs and sp[1] == "s"):
            return self.irregular_verbs[verb]
        elif(verb in self.irregular_verbs and sp[1] == "p"):
            if self.irregular_verbs[verb][-1] == "a":
                return self.irregular_verbs[verb][:-1] + "eni"
            else:
                return self.irregular_verbs[verb] + "ni"

    def to_imperfect(self, verb, is_neg, sp):
        return ""
    def method_dispatcher(self,method_name):
        methods = {"PAST":self.to_past, "PRES":self.to_present, "FUT":self.to_future, 
                    "PERF":self.to_past_perfect, "IMP":self.to_imperitive}
        return methods[method_name]
    def generate_sentence(self, features):
        feats = features.split("+")
        verb = feats[-1]
        if feats[0] == "NEG":
            sp = feats[1]
            tense = feats[2]
            is_neg = True
        else:
            sp = feats[0]
            tense = feats[1]
            is_neg = False
        return self.method_dispatcher(tense)(verb, is_neg, sp)
