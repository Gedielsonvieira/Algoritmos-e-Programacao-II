from Automovel import *

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = int(qtdPortas)
    
    def imprimirInformacoes(self):
        print(f''' 
        
    --- CARRO ---
    Marca: {self.marca} 
    Quantidade de Rodas: {self.qtdRodas} 
    Modelo: {self.modelo} 
    Velocidade: {self.velocidade} km/h
    Potencia do Motor: {self.potenciaDoMotor} cc
    Quantidade de Portas: {self.qtdPortas}''')
