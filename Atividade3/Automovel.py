from Veiculo import *

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoes(self):
        print(f''' 
    
    --- AUTOMÓVEL ---
    Marca: {self.marca} 
    Quantidade de Rodas: {self.qtdRodas} 
    Modelo: {self.modelo} 
    Velocidade: {self.velocidade} km/h
    Potencia do Motor: {self.potenciaDoMotor} cc''')
       

