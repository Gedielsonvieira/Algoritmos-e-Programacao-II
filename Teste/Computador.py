from abc import ABCMeta, abstractmethod

class Computador(metaclass = ABCMeta):

    @property
    def modelo(self):
        pass
#-----------------------------

    @property
    def cor(self):
        pass

#-----------------------------  

    @property
    def preco(self):
        pass

#----------------------------
   
    def getInformacoes(self):
        pass

    @abstractmethod
    def cadastrar(self):
        pass