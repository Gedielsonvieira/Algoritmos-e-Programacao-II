from Veiculo import *

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = int(numMarchas)
        self.bagageiro = bool(bagageiro)
    
    def imprimirInformacoes(self):
        print(f'''--- BICICLETA ---
    Marca: {self.marca} 
    Quantidade de Rodas: {self.qtdRodas} 
    Modelo: {self.modelo} 
    Velocidade: {self.velocidade} km/h
    Número de Marchas: {self.numMarchas}
    Bagageiro: {self.bagageiro}''')
        
        

