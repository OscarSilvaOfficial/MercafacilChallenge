from flask import request, abort
import sqlalchemy
from api.models.user import User
from flask.views import MethodView
from api.utils.request import parse_request
from api.utils.auth import encode_password
from api.views.users.parser import parser


class UserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    request['password'] = encode_password(request['password']) 
    user = User(**request)

    try:
      user.save()
    except sqlalchemy.exc.IntegrityError as e:
      abort(409, "User already exists")
    except Exception as e:
      abort(500, "Internal server error on create user")
    
    return user.to_dict(), 201 