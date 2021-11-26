from jwt import encode, decode, DecodeError
from api.config import SECRET
from api.interfaces.cryptography import Cryptography


class Validations(Cryptography):

  @staticmethod
  def encrypt_token(token):
    return Validations()._encrypt(token)

  @staticmethod
  def decrypt_token(token):
    return Validations()._validate(token)
  
  def _validate(self, data):
    try:
      return decode(data, SECRET, algorithms=['HS256'])
    except DecodeError:
      return False

  def _encrypt(self, data):
    return encode(data, SECRET, algorithm='HS256')