from api.core.validators.email_validator import EmailValidator
from api.core.validators.phone_number_validator import PhoneNumberValidator
from api.ports.validators_port import ValidatorsPort


class ValidatorRoot(ValidatorsPort):
  
  def __init__(self, customer):
    self.__customer = customer

  def validate(self):
    email = EmailValidator(self.__customer.email)
    email.validate()
    
    for contact in self.__customer.contacts:
      phone = PhoneNumberValidator(contact['phone'])
      phone.validate()
  