'''
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
'''

class Veiculo():
    
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = str(marca)
        self.qtdRodas = int(qtdRodas)
        self.modelo = str(modelo)
        self.velocidade = velocidade
    
    def imprimirInformacoes(self):
        print(f'''--- VEÍCULO ---
    Marca: {self.marca} 
    Quantidade de Rodas: {self.qtdRodas} 
    Modelo: {self.modelo} 
    Velocidade: {self.velocidade} km/h''')
        
    def acelerar(self, velocidadeAtual):
        self.velocidade = self.velocidade + velocidadeAtual

    def frear(self, velocidadeAtual):
        self.velocidade = self.velocidade - velocidadeAtual

