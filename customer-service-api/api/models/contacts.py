from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin


class Contacts(SerializerMixin):

  serialize_only = ('id', 'nome', 'celular')

  id = Column(Integer, primary_key=True)
  _nome = Column('nome', String(255), nullable=False)
  _celular = Column('celular', String(255), nullable=False)

  @staticmethod
  def get(filter_by):
    try:
      user = Contacts.query.filter_by(**filter_by).first()
    except Contacts.DoesNotExist:
      return {'message': 'Contact does not exist'}, 404
    return user