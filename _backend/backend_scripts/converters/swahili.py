from .converter import TenseConverter


class SwahiliConverter(TenseConverter):
    
    def __init__(self) -> None:
        super().__init__()
        # add any exception files here
        
                
    def to_past(self, verb, is_neg):
        return ""
    def to_present(self,verb, is_neg):
        return ""
    def to_future(self, verb, is_neg):
        return ""

    def to_past_perfect(self, verb, is_neg):
        return ""
    
    def to_imperfect(self, verb):
        return ""
    
    def generate_sentence(self, **args):
        return super().generate_sentence(**args)