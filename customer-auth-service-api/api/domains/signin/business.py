from api.models.user import User
from api.domains.users.validaitons import Validations as UserValidations
from api.domains.token.validaitons import Validations as TokenValidations
from flask import Response
from flask import abort

class SignIn:

  def __init__(
    self, 
    user_validations=UserValidations, 
    token_validations=TokenValidations
  ):
    self._user_validations: UserValidations = user_validations
    self._token_validations: TokenValidations = token_validations

  def validate_signin(self, email, password): 
    user = User.get({ 'email': email })

    if not user: abort(401, 'Invalid credentials')

    user_validation = self._user_validations(
      password=password,
      hash=user.password
    )

    if not user_validation.validate_password():
      return abort (401, 'Invalid credentials')

    token = self._generate_token(user)

    return self._response(token)

  def _generate_token(self, user):
    return self._token_validations.encrypt_token({
      'id': user.id,
      'email': user.email,
      'name': user.name,
      'password': user.password
    })

  def _response(self, authentication_token):
    return Response(
      status=204, 
      mimetype='application/json',
      headers={ 
        'Authentication-Token': authentication_token,
        'Access-Control-Expose-Headers': 'Authentication-Token' 
      }, 
    )