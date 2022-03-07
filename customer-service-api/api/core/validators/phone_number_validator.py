import phonenumbers

from ports.validators_port import ValidatorsPort

class InvalidPhoneNumberException(Exception):
  pass

class PhoneNumberValidator(ValidatorsPort):
  
  def __init__(self, phone):
    self.__phone = phonenumbers.parse(phone, 'BR')
    
  def __validate_contact_phone(self) -> None:
    if not phonenumbers.is_valid_number(self.__phone):
      phone = phonenumbers.format_number(self.__phone, phonenumbers.PhoneNumberFormat.NATIONAL)
      raise InvalidPhoneNumberException(f'Invalid phone number {phone}')
    
  def validate(self):
    self.__validate_contact_phone()