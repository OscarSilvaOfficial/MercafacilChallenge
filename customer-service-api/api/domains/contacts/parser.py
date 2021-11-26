from flask import abort
from api.utils.auth import is_authenticated
from api.utils.format import parse_customer


def parser(request):
  validation = is_authenticated(request) 
  
  if not request.headers.get('authentication-token'):
    return abort(401, 'Missing authentication-token header')

  if request.json.get('contacts'):
    contacts = request.json.get('contacts')
    return parse_many_contacts(contacts, validation.get('email'))
  else:
    contact = request.json
    return parse_contact(contact, validation.get('email'))

def parse_contact(contact, auth_email):
  if not contact.get('name'):
    return abort(400, 'Missing name field')

  if not contact.get('cellphone'):
    return abort(400, 'Missing cellphone field')
  
  new_contact = {
    'contato': {
      'nome': contact.get('name'),
      'celular': contact.get('cellphone'),
    },
    'cliente': parse_customer(auth_email)  
  }

  return new_contact

def parse_many_contacts(contacts, auth_email):
  new_contacts = []

  for contact in contacts:
    if not contact.get('name'):
      return abort(400, 'Missing name field')

    if not contact.get('cellphone'):
      return abort(400, 'Missing cellphone field')

    new_contacts.append({
      'nome': contact.get('name'),
      'celular': contact.get('cellphone'),
    })

  return {
    'contatos': new_contacts,
    'cliente': parse_customer(auth_email)  
  }