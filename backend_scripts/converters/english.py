from .converter import TenseConverter


class EnglishConverter(TenseConverter):
    
    def __init__(self, past_tense_exc:dict, past_participle_exc:dict) -> None:
        super().__init__()
        self.past_tense_exc = past_tense_exc
        self.past_participle_exc = past_participle_exc
        
    def to_past(self, verb, is_neg):
        if is_neg:
            return "did not " + verb

        if len(verb.split(" ")) > 1:
            return self.to_past(verb.split(" ")[0], is_neg) + " " + " ".join(verb.split(" ")[1:])
        elif verb.startswith("be "):
            return verb.replace("be ", "was ")
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

    def to_present(self,verb, is_neg):
        if is_neg:
            return "do not " + verb
        return verb

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


    def to_past_perfect(self, verb, is_neg):
        if is_neg:
            _not = " not"  # using _not to prevent name clash with python's not keyword
        else:
            _not = ""

        if verb.startswith("be "):
            return f"have{_not} been " + verb[3:]
        elif len(verb.split(" ")) > 1:
            return f"have{_not} " + self.get_past_participle(verb.split(" ")[0]) + " " + " ".join(verb.split(" ")[1:])
        return f"have{_not} " + self.get_past_participle(verb)

    def to_imperfect(self, verb):
        # does not exist in english
        return None