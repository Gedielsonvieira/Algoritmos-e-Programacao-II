from Automovel import *

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.__partidaEletrica = bool(partidaEletrica)
    
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f''' 
    Partida Eletrica: {self.__partidaEletrica}''')