from requests import post
from flask import abort
from api.config import AUTH_SERVICE_API

def is_authenticated(request):
  """
  Verify auth token
  """
  token = request.headers.get('authentication-token', None)
  validation = post(
    f'{AUTH_SERVICE_API}/api/token/validate', 
    headers={'authentication-token': token}
  )

  if validation.status_code != 200:
    return abort(401, 'Invalid authentication token')

  return validation.json()
    