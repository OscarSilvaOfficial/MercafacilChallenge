from abc import ABC


class DB(ABC):
  
  def select_all(self, where: dict) -> list:
    pass
  
  def insert(self, table_columns: list, insert_values: tuple):
    pass
    
  def update(self, set: dict, where: dict):
    pass
    
  def delete(self, where: dict):
    pass