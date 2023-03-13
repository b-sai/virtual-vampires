from abc import ABC, abstractmethod

class TenseConverter(ABC):
    
    def __init__(self) -> None:
        super().__init__()
            
    @abstractmethod  
    def to_past(**args):
        pass
    
    @abstractmethod
    def to_present(**args):
        pass
    
    @abstractmethod
    def to_future(**args):
        pass
    
    @abstractmethod
    def to_past_perfect(**args):
        pass

    @abstractmethod
    def to_imperfect(**args):
        pass

        
    