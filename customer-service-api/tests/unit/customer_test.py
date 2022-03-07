import phonenumbers
from api.core.customer import Customer
from api.core.validators.phone_number_validator import InvalidPhoneNumberException
import logging, re

LOGGER = logging.getLogger(__name__)

def test_valid_macapa_customer():
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
    assert contact['phone'][0:3] == '+55' \
      and contact['phone'][4:5] == '(' and contact['phone'][7:8] == ')' \
      and contact['phone'][14:15] == '-' and len(contact['phone']) == 19
      
def test_valid_varejao_customer():
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
    assert len(contact['phone']) == 13 and contact['phone'][0:2] == '55'

def test_invalid_macapa_customer():
  try:
    Customer(
      email="cliente@gmail.com.br",
      customer_name="macapa",
      contacts=[
        {"phone": "+55119999999991", "name": "Geralt de Rivia"},
        {"phone": "479346329341", "name": "Ermanoteu"},
        {"phone": "+55 (47) 93463-92931", "name": "Mikalateia"},
      ]
    )
  except Exception as e:
    assert type(e) is InvalidPhoneNumberException
    
def test_invalid_varejao_customer():
  try:
    Customer(
      email="cliente@gmail.com.br",
      customer_name="varejao",
      contacts=[
        {"phone": "+55119999999991", "name": "Geralt de Rivia"},
        {"phone": "479346329341", "name": "Ermanoteu"},
        {"phone": "+55 (47) 93463-92931", "name": "Mikalateia"},
      ]
    )
  except Exception as e:
    assert type(e) is InvalidPhoneNumberException

  
  