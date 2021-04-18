class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = int(codigo) #private
        self.nome = nome
        self._endereco = endereco #protected
        self.__telefone = str(telefone) #private
    
    def imprimeNome(self):
        print(f'Nome: {self.nome}')

    def __imprimeTelefone(self):#Método Private
        print(f'Telefone: {self.__telefone}')