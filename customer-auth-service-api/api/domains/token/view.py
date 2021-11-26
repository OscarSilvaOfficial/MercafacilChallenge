from flask import request
from flask.views import MethodView
from api.utils.request import parse_request
from api.domains.token.parser import parser
from .business import Token

class TokenView(MethodView, Token):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    return self.create_token(**request)