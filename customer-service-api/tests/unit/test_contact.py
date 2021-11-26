from api.domains.contacts.business import CreateContacts

class TestContact:

  def test_create_contacts_varejao(self):
    request = {
      'cliente': 'varejao',
      'contatos': [
        {
          'nome': 'Teste',
          'celular': '5511999999999',
        },
        {
          'nome': 'Teste',
          'celular': '+55 (11) 999999999',
        },
        {
          'nome': 'Teste',
          'celular': '5511999999999',
        },
        {
          'nome': 'Teste',
          'celular': '+55 (11) 999999999',
        },
      ]
    }
    contacts = CreateContacts()
    data = contacts.create_contacts(request)
    assert len(data) == 4

  def test_create_contacts_macapa(self):
    request = {
      'cliente': 'macapa',
      'contatos': [
        {
          'nome': 'Teste',
          'celular': '5511999999999',
        },
        {
          'nome': 'Teste',
          'celular': '+55 (11) 999999999',
        },
        {
          'nome': 'Teste',
          'celular': '5511999999999',
        },
        {
          'nome': 'Teste',
          'celular': '+55 (11) 999999999',
        },
      ]
    }
    contacts = CreateContacts()
    data = contacts.create_contacts(request)
    assert len(data) == 4