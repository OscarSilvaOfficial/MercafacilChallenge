import re

from ports.validators_port import ValidatorsPort

class InvalidEmailException(Exception):
  pass

class EmailValidator(ValidatorsPort):
  
  def __init__(self, email):
    self.__email = email
    
  def validate(self):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', self.__email):
      raise InvalidEmailException(f'Invalid email {self.__email}')