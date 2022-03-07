from fast_sql_manager.implementations.postgres import PostgresRepository

from ports.db import DB


class Postgres(DB):
  
  def __init__(self, host: str, port: int, user: str, passwd: str, db_name: str, table_name: str) -> None:
    self.__table_name = table_name
    self.postgres_driver = PostgresRepository(host, port, user, passwd, db_name)
    
  def select_all(self, where: dict=None) -> list:
    if where is None:
      return self.postgres_driver.select_all(self.__table_name)
    return self.postgres_driver.select_all(self.__table_name, where)
  
  def insert(self, table_columns: list, insert_values: tuple):
    return self.postgres_driver.insert(self.__table_name, table_columns, insert_values)
    
  def update(self, set: dict, where: dict):
    return self.postgres_driver.update(self.__table_name, set, where)
    
  def delete(self, where: dict):
    return self.postgres_driver.delete(self.__table_name, where)
  