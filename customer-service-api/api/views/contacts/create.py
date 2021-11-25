from api.models.varejao import Varejao
from api.models.macapa import Macapa

class CreateContacts:

  def create_contacts(self, request):
    """
    Create a new contact
    """
    client = request.get('cliente')
    clients = {
      'macapa': Macapa,
      'varejao': Varejao,
    }

    if request.get('contatos'):
      response = []
      for contact in request.get('contatos'):
        saved_contact = clients[client](**contact).save()
        response.append(saved_contact.to_dict())
      return response
    else:
      entity = clients[client](**request.get('contato'))
      response = entity.save()
      return response.to_dict()