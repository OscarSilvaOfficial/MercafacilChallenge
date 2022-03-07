from abc import ABC, abstractmethod

class ValidatorsPort(ABC):
  
    @abstractmethod
    def validate(self):
        pass
    