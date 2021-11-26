from passlib.hash import bcrypt
from api.interfaces.cryptography import Cryptography


class Validations(Cryptography):

  def __init__(self, password, hash=None) -> None:
    self._password = password
    self._hash = hash
  
  def validate_password(self):
    if self._password is None: raise Exception('Hash password is required')
    return self._validate(self._password)

  def encrypt_password(self):
    return self._encrypt(self._password)
  
  def _validate(self, data):
    try:
      return bcrypt.verify(data, self._hash)
    except Exception:
      return False

  def _encrypt(self, data):
    return bcrypt.hash(data)