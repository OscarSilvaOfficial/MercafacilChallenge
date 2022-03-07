from api.core.validators.validator_root import ValidatorRoot
import phonenumbers, re
from typing import NewType

from api.ports.validators_port import ValidatorsPort


Email = NewType('Email', str)
Contacts = NewType('Contacts', list[dict])

class Customer:
  
  def __init__(self, email: Email, customer_name: str, contacts: Contacts, validator: ValidatorsPort=ValidatorRoot) -> None:
    self.__customer_name = customer_name
    self.__email = email
    self.__contacts = self.__convert_contact(contacts)
    self.__validator = validator(self)
    self.__validator.validate()
    
  def __convert_contact(self, contacts: dict) -> dict:
    for contact in contacts:
      contact['phone'] = self.__standardize_contact_phone(contact['phone'])
      contact['name'] = self.__standardize_contact_name(contact['name'])
    return contacts
    
  def __standardize_contact_phone(self, phone: str) -> None:
    
    phone = phonenumbers.parse(phone, 'BR')
    phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL)
    
    if "+55" not in phone:
      phone = "+55 " + phone
    
    formated_phone = {
      "varejao": re.sub('[^0-9]', '', phone),
      "macapa" : phone,
    }
      
    return formated_phone[self.__customer_name]
  
  def __standardize_contact_name(self, name: str) -> None:
    
    formated_name = {
      "varejao": name,
      "macapa" : name.upper(),
    }
    
    return formated_name[self.__customer_name]
  
  @property
  def email(self) -> Email:
    return self.__email
  
  @property
  def customer_name(self) -> str:
    return self.__customer_name
  
  @property
  def contacts(self) -> Contacts:
    return self.__contacts