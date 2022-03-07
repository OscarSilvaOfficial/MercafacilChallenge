import phonenumbers

from api.ports.phone_formater_port import PhoneFormaterPort

class PhoneFormater(PhoneFormaterPort):
  
  def __init__(self, phone: str) -> None:
    self.__phone = phonenumbers.parse(phone, 'BR')

  def format(self):
    return phonenumbers.format_number(self.__phone, phonenumbers.PhoneNumberFormat.NATIONAL)
  
  def validate_phone(self):
    return phonenumbers.is_valid_number(self.__phone)
