from abc import ABC, abstractmethod

class Cryptography(ABC):

    @abstractmethod
    def _encrypt(self, data):
      pass

    @abstractmethod
    def _validate(self, data):
      pass