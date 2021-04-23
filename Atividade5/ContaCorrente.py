from ContaBancaria import *

class ContaCorrente(ContaBancaria):
    def __init__(self, agencia, conta, cpf, banco, deposito = 0):
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.banco = banco
        self._deposito = deposito

    def cadastrar(self):
        conta = [self.agencia, self.conta, self.cpf, self.banco]
        print(conta)
    
    def depositar(self, value):
        if isinstance(value, str):
            valor = float(value.replace('R$', ''))
            self._deposito = self._deposito + valor
        else:
            self._deposito = self._deposito + value 
        print(self._deposito)


c = ContaCorrente(123, 165165, 16516516, 'nu')
c.cadastrar()
c.depositar(1000)
