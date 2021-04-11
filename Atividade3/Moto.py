from Automovel import *

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = bool(partidaEletrica)
    
    def imprimirInformacoes(self):
        print(f''' --- MOTO ---
    Marca: {self.marca} 
    Quantidade de Rodas: {self.qtdRodas} 
    Modelo: {self.modelo} 
    Velocidade: {self.velocidade} km/h
    Potencia do Motor: {self.potenciaDoMotor} cc
    Partida Eletrica: {self.partidaEletrica}''')