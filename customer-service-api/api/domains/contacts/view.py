from flask import request
from flask.views import MethodView
from api.utils.request import parse_request
from api.domains.contacts.parser import parser
from api.domains.contacts.business import CreateContacts


class ContactView(MethodView, CreateContacts):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    return self.create_contacts(request)