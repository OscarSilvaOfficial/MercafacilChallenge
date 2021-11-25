from flask import request
from flask.views import MethodView
from flask import abort
from api.models.user import User
from api.utils.auth import encode_token, validate_password
from api.utils.request import parse_request
from api.views.signin.parser import parser
from flask import Response

class SignInView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    email = request.get('email')
    user = User.get({ 'email': email })
    password = request.get('password')

    if not user:
      abort(401, 'Invalid credentials')

    if not validate_password(password, user.password):
      return abort (401, 'Invalid credentials')

    token = encode_token({
      'id': user.id,
      'email': user.email,
      'name': user.name,
      'password': user.password
    })

    headers = { 
      'Authentication-Token': token,
      'Access-Control-Expose-Headers': 'Authentication-Token' 
    }

    response = Response('Sign process', headers=headers, status=200, mimetype='application/json')

    return response