from Computador import *

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self._modelo = modelo
        self._cor = cor
        self._preco = float(preco)
        self.__tempoDeBateria = tempoDeBateria
        
#-----------------------------

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

#-----------------------------

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

#-----------------------------

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

#-----------------------------

    def cadastrar(self):
        print('Notebook cadastrado')

    def getInformacoes(self):
        return 'Modelo: {}\nCor: {}\nPreço: {:.3f}\nPotência da fonte: {}\n'.format(self._modelo,self._cor,self._preco,self.__tempoDeBateria)