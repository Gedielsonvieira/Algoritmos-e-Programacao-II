from Veiculo import *

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.__numMarchas = int(numMarchas)
        self.__bagageiro = bool(bagageiro)
    
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f'''
    Número de Marchas: {self.__numMarchas}
    Bagageiro: {self.__bagageiro}''')

        
        

