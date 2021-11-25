from api.models import Base, db
from api.utils.format import cellphone_varejao_format
from .contacts import Contacts


class Varejao(Base, Contacts):

  __tablename__ = 'contacts'
  __table_args__ = {'extend_existing': True}
  __bind_key__ = 'varejao'

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome.lower()

  @property
  def celular(self):
    return self._celular

  @celular.setter
  def celular(self, celular):
    self._celular = cellphone_varejao_format(celular)

  def save(self):
    db['postgres'].add(self)
    db['postgres'].commit()
    return self
