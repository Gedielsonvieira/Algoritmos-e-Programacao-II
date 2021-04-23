# informa que essa classe é abstrata Abstract basec class
from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass = ABCMeta):
    
    @abstractmethod # informa que o método a seguir é um método abstrato
    def cadastrar(self):
        pass
    
    @abstractmethod 
    def depositar(self, value):
        pass