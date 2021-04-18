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

'''Quando se utilizar modificadores se acesso: '''
# Cria-se método set para cada atributo que se quer permitir que seja modificado fora da própia classe

'''
No diagrama de classe:
O sinal de - é privado (__) -> só pode ser modificado e acessado dentro da sua própia classe
O sinal de # é protegido (_) -> só pode ser acessado e modificado dentro da própria classe e nas classes que herdam destas classes e classes dentro do mesmo pacote
O sinal de + é publico -> pode ser acessado e modificado dentro de qualquer classe do projeto
'''

#pacote é um diretório que dentro deste diretório tem um conjunto de classes 
#Pacote é um conjunto de classes que estão no mesmo diretório
#Pacote é um diretório -> dentro do diretório tem arquivos -> dentro de arquivos tem as classes que por sua vez tem a estrutura de dados.