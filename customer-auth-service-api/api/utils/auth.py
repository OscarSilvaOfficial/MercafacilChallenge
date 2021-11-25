from passlib.hash import bcrypt
from api.models.user import User
from api.config import SECRET
from jwt import decode, encode, DecodeError

def encode_password(password, *args, **kwargs):
  """
  Encode a password
  """
  return bcrypt.hash(password)

def validate_password(password, hash):
  try:
    return bcrypt.verify(password, hash)
  except Exception:
    return False

def encode_token(payload):
  """
  Encode a token using the SECRET key
  """
  return encode(payload, SECRET, algorithm='HS256')

def validate_token(token):
  """
  Validate a token using the SECRET key
  """
  try:
    token = decode(token, SECRET, algorithms=['HS256'])
  except DecodeError:
    return False

  user = User.get({'email': token['email']})

  if user.password != token['password']:
    return False
  
  return user