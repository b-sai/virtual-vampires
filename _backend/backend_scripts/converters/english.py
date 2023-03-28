from .converter import TenseConverter


class EnglishConverter(TenseConverter):
    
    def __init__(self, past_tense_exc:dict, past_participle_exc:dict) -> None:
        super().__init__()
        self.past_tense_exc = past_tense_exc
        self.past_participle_exc = past_participle_exc
        
    def to_past(self, verb, is_neg, sp):
        if is_neg:
            return "did not " + verb

            
        if verb == "be":
            if sp in ["1s", "3s"]:
                # I/(s)he was happy
                return "was"
            else:
                # They were happy
                return "were"

        if len(verb.split(" ")) > 1:
            return self.to_past(verb.split(" ")[0], is_neg, sp) + " " + " ".join(verb.split(" ")[1:])
        elif verb.startswith("put on"):
            return verb

        if verb in self.past_tense_exc:
            return self.past_tense_exc[verb]
        elif verb.endswith("e"):
            return verb + "d"
        elif verb.endswith("y"):
            return verb[:-1] + "ied"
        elif verb.endswith("d"):
            return verb[:-1] + "t"
        else:
            return verb+"ed"

    def to_present(self,verb:str, is_neg:bool, sp: str):
        """
        p is plurality. If we have 2p, we want are, not do and so on
        
        """
        
        
        if sp == "3s" and " " not in verb:
            verb = self.get_plural(verb)
        elif sp == "3s" and " " in verb:
            # multiple words, need to convert only first word to plural
            # put on weight -> puts on weight
            verb = self.get_plural(verb.split(" ")[0]) + " " + " ".join(verb.split(" ")[1:])
        
        if is_neg:
            p_part = "do "
        else:
            p_part = ""
            
        if verb.startswith("be "):
            if sp == "1s":
                p_part = "am "
            elif sp == "1p":
                p_part = "are "
            elif sp == "2s":
                p_part = "are "
            elif sp == "2p":
                p_part = ""
            elif sp == "3s":
                p_part = "is "
            elif sp == "3p":
                p_part = "are "
            verb = verb[3:]
        
        if is_neg:

            return f"{p_part}not {verb}"
        return f"{p_part}{verb}"

    def to_future(self, verb, is_neg):
        if is_neg:
            _not = " not"
        else:
            _not = ""

        return f"will{_not} " + verb
    

    def get_past_participle(self, verb):
        if verb in self.past_participle_exc:
            return self.past_participle_exc[verb]
        elif verb.endswith("e"):
            return verb + "d"
        elif len(verb) > 2 and verb.endswith("y") and verb[-2] not in "aeiou":
            return verb.replace("y", "ied")
        else:
            return verb+"ed"


    def to_past_perfect(self, verb, is_neg, sp):
        if is_neg:
            _not = " not"  # using _not to prevent name clash with python's not keyword
        else:
            _not = ""
            
        if sp == "3s":
            prefix = "has"
        else:
            prefix = "have"

        if verb.startswith("be "):
            return f"{prefix}{_not} been " + verb[3:]
        elif len(verb.split(" ")) > 1:
            return f"{prefix}{_not} " + self.get_past_participle(verb.split(" ")[0]) + " " + " ".join(verb.split(" ")[1:])
        return f"{prefix}{_not} " + self.get_past_participle(verb)

    def to_imperfect(self, verb):
        # does not exist in english
        return None
    
    def to_s(self, verb:str, s: str):
        s_part = ""
        
        if s.startswith("1"):
            s_part = "I"
        elif s.startswith("2"):
            s_part = "you"
        elif s.startswith("3"):
            s_part = "(s)he"
            
        return s_part
    
    def get_plural(self, verb:str):
        if verb == "be":
            return "is"
        if verb.endswith("y") and verb[-2] not in "aeiou":
            return verb[:-1] + "ies"
        elif verb.endswith(("s", "x", "z", "sh", "ch")):
            return verb + "es"
        else:
            return verb + "s"

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
                result += " " + self.to_past(verb, is_neg, sp)
            elif feat == 'FUT':
                result += " " + self.to_future(verb, is_neg)
            elif feat == 'PERF':
                result += " " + self.to_past_perfect(verb, is_neg, sp)
            elif feat == 'PRES':
                result += " " + self.to_present(verb, is_neg, sp)

            elif feat in ["1s", "2s", "3s"]:
                result += self.to_s(verb, feat)
                sp = feat
            elif feat == "1p":
                result += "we"
                sp = feat
            elif feat == "2p":
                result += "ye"
                sp = feat
            elif feat == "3p":
                result += "they"
                sp = feat
            elif feat == "NEG":
                is_neg = True

        return result
