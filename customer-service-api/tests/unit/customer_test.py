import phonenumbers
from api.core.customer import Customer
import logging

LOGGER = logging.getLogger(__name__)

def test_macapa_customer():
  customer = Customer(
    email="cliente@gmail.com.br",
    customer_name="macapa",
    contacts=[
      {"phone": "+5511999999999", "name": "Geralt de Rivia"},
      {"phone": "47934632934", "name": "Ermanoteu"},
      {"phone": "+55 (47) 93463-9293", "name": "Mikalateia"},
    ]
  )
  
  for contact in customer.contacts:
    LOGGER.info(contact)
    assert contact['name'].isupper()
    assert phonenumbers.is_valid_number(phonenumbers.parse(contact['phone'], 'BR'))
    
def test_varejao_customer():
  customer = Customer(
    email="cliente@gmail.com.br",
    customer_name="varejao",
    contacts=[
      {"phone": "+5511999999999", "name": "Geralt de Rivia"},
      {"phone": "47934632934", "name": "Ermanoteu"},
      {"phone": "+55 (47) 93463-9293", "name": "Mikalateia"},
    ]
  )
  
  for contact in customer.contacts:
    LOGGER.info(contact)
    assert phonenumbers.is_valid_number(phonenumbers.parse(contact['phone'], 'BR'))

  
  