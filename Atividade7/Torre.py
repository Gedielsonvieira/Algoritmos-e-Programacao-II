class Torre:
    
    def __init__(self, id, nome, endereco):
        self.id = int(id)
        self.nome = str(nome)
        self.endereco = str(endereco)
   
    def imprimir(self):
        print(self.id, self.nome, self.endereco)