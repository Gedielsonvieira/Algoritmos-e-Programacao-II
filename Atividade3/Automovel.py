from Veiculo import *

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.__potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f''' 
    Potencia do Motor: {self.__potenciaDoMotor} cc''')

