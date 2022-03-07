from abc import ABC, abstractmethod

class PhoneFormaterPort(ABC):
  
  @abstractmethod
  def format(self):
    pass
  
  @abstractmethod
  def validate_phone(self):
    pass