import phonenumbers

from api.infra.formaters.phone_formater import PhoneFormater
from api.ports.phone_formater_port import PhoneFormaterPort
from api.ports.validators_port import ValidatorsPort

class InvalidPhoneNumberException(Exception):
  pass

class PhoneNumberValidator(ValidatorsPort):
  
  def __init__(self, phone, formater: PhoneFormaterPort=PhoneFormater):
    self.__phone_formater = formater(phone)
    
  def __validate_contact_phone(self) -> None:
    if not self.__phone_formater.validate_phone():
      phone = self.__phone_formater.format()
      raise InvalidPhoneNumberException(f'Invalid phone number {phone}')
    
  def validate(self):
    self.__validate_contact_phone()