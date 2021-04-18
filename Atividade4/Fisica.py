#herda da classe Pessoa
from Pessoa import *

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = float(altura)

    def imprimeCPF(self):
        print(f'CPF: {self.__cpf}')
    
    def __calculaIMC(self):
        calculoIMC = self.peso / (self.altura**2)
        print('IMC: {:.1f}'.format(calculoIMC))