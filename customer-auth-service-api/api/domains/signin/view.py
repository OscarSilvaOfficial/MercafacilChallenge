from flask import request
from flask.views import MethodView
from api.utils.request import parse_request
from api.domains.signin.parser import parser
from .business import SignIn

class SignInView(MethodView, SignIn):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    return self.validate_signin(**request)