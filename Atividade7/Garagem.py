from Apartamento import Apartamento

class Garagem:
    def __init__(self):
        self.inicio = None #1° elemento da fila
        self.fim = None    #Ultimo elemento da fila
        self.size = 0      #fila tem um tamanho
    
    def inserir(self, id, numero, Torre, vaga):
        print("inserindo apt id",id)
        apt = Apartamento(id, numero, Torre, vaga)
        if self.fim is None:
            self.fim = apt
        else:
            self.fim.proximo = apt
            self.fim = apt
        if self.inicio is None:
            self.inicio = apt
            
        self.size = self.size + 1
        
    def __len__(self):
        return self.size

    def imprimir(self): 
        if( self.inicio == None ) :
            print( "Fila Vazia")
        else:
            aux = self.inicio
            while ( aux  ) :
                aux = aux.proximo
            print("Tamanho da Fila: ", self.size)

    def remover(self) :
        if self.size == 0 :
            print("Fila vazia")
        if self.size > 0:
            print(f"Apartamento de ID: {self.inicio.id} receberá a vaga: {self.inicio.vaga}")
            elemento = self.inicio
            self.inicio =self.inicio.proximo
            self.size -= 1
            return self.inicio