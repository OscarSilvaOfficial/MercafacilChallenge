from api.models.user import User
from .validaitons import Validations
from api.models.user import User
from flask import abort

class Token:

  def __init__(self, validations=Validations):
    self._validations: Validations = validations

  def create_token(self, authentication_token):
    validation = self._validate_token(authentication_token)
    return validation.to_dict()

  def _validate_token(self, token):

    token = self._validations.decrypt_token(token)

    if not token:
      abort(401, 'Invalid authentication token')

    user = User.get({'email': token.get('email')})

    if user.password != token['password']:
      abort(401, 'Invalid authentication')
    
    return user