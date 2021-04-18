'''
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
'''

class Veiculo():
    
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.__marca = str(marca)
        self.__qtdRodas = int(qtdRodas)
        self.__modelo = str(modelo)
        self.__velocidade = velocidade
    
    def imprimirInformacoes(self):
        print(f'''

    --- VEÍCULO ---
    Marca: {self.__marca} 
    Quantidade de Rodas: {self.__qtdRodas} 
    Modelo: {self.__modelo} 
    Velocidade: {self.__velocidade} km/h''', end='')
        
    def acelerar(self, velocidadeAtual):
        self.__velocidade = self.__velocidade + velocidadeAtual

    def frear(self, velocidadeAtual):
        self.__velocidade = self.__velocidade - velocidadeAtual