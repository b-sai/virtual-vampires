from abc import ABC, abstractmethod

class TenseConverter(ABC):
    
    def __init__(self) -> None:
        super().__init__()
            
    @abstractmethod  
    def to_past(self, **args):
        pass
    
    @abstractmethod
    def to_present(self, **args):
        pass
    
    @abstractmethod
    def to_future(self, **args):
        pass
    
    @abstractmethod
    def to_past_perfect(self, **args):
        pass

    @abstractmethod
    def to_imperfect(self, **args):
        pass
    
    @abstractmethod
    def generate_sentence(self, **args):
        pass
        
    