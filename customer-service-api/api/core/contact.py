class Contact:
  
  def __init__(self, name: str, phone: str) -> None:
    self.__name = name
    self.__phone = phone
    
  @property
  def name(self) -> str:
    return self.__name
  
  @property
  def phone(self) -> str:
    return self.__phone