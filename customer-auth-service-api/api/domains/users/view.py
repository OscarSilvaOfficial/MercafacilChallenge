from flask import request, abort
import sqlalchemy
from api.models.user import User
from flask.views import MethodView
from api.utils.request import parse_request
from api.domains.users.parser import parser
from .business import User as UserBusinessLayer


class UserView(MethodView, UserBusinessLayer):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    return self.create_user(**request)