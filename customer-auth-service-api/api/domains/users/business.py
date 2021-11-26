import sqlalchemy
from flask import abort
from .validaitons import Validations
from api.models.user import User as UserModel

class User:

  def __init__(self, validations=Validations) -> None:
      self._validations: Validations = validations

  def create_user(self, name, email, password):
    password = self._validations(password)

    user = UserModel(
      name=name,
      email=email, 
      password=password.encrypt_password()
    )

    try:
      user.save()
    except sqlalchemy.exc.IntegrityError:
      abort(409, "User already exists")
    except Exception as e:
      abort(500, "Internal server error on create user")
    
    return user.to_dict(), 201 
