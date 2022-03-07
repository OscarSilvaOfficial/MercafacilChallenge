from abc import ABC


class DB(ABC):
  
  def select_all(self, where: dict) -> list:
    pass
  
  def insert(self, table_columns: list, insert_values: tuple) -> None:
    pass
    
  def update(self, set: dict, where: dict) -> None:
    pass
    
  def delete(self, where: dict) -> None:
    pass