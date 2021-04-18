class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = int(codigo) #private
        self.nome = nome
        self._endereco = endereco #protected
        self.__telefone = str(telefone) #private
    
    def imprimeNome(self):
        print(f'Nome: {self.nome}')

    def __imprimeTelefone(self):#Método Private
        print(f'Telefone: {type(self.__telefone)}')

    
#self é sempre o objeto que estiver utilizando o método
#set é para modificar o valor de um atributo
#get é para pegar alguma informação

'''
p = Pessoa(1, 'nifw', 'swfgr', 16513616)
p._Pessoa__imprimeTelefone()
'''