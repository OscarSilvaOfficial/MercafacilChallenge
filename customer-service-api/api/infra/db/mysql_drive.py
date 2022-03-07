from fast_sql_manager.implementations.mysql import MySQLRepository

from ports.db import DB


class MySql(DB):
  
  def __init__(self, host: str, port: int, user: str, passwd: str, db_name: str, table_name: str) -> None:
    self.__table_name = table_name
    self.mysql_driver = MySQLRepository(host, port, user, passwd, db_name)
    
  def select_all(self, where: dict=None) -> list:
    if where is None:
      return self.mysql_driver.select_all(self.__table_name)
    return self.mysql_driver.select_all(self.__table_name, where)
  
  def insert(self, table_columns: list, insert_values: tuple):
    return self.mysql_driver.insert(self.__table_name, table_columns, insert_values)
    
  def update(self, set: dict, where: dict):
    return self.mysql_driver.update(self.__table_name, set, where)
    
  def delete(self, where: dict):
    return self.mysql_driver.delete(self.__table_name, where)
  