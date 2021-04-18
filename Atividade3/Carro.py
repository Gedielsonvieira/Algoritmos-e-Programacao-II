from Automovel import *

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.__qtdPortas = int(qtdPortas)
    
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f''' 
    Quantidade de Portas: {self.__qtdPortas}''')
