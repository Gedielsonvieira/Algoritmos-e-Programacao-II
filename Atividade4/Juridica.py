#herda da classe Pessoa
from Pessoa import *
from datetime import date

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscricaoEstadual, qtdFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__CNPJ = CNPJ
        self.__inscricaoEstadual = inscricaoEstadual
        self.qtdFuncionarios = int(qtdFuncionarios)

    def imprimeCNPJ(self):
        return self.__CNPJ

    def __emitirNotaFiscal(self):
        print(f'''
Cupom Fiscal
Empresa: {self.__inscricaoEstadual}    
Endereço: {self._endereco}
CNPJ: {self.__CNPJ} 
Data: {date.today()}
''')