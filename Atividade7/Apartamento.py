from Torre import Torre

class Apartamento:
    
    def __init__(self, id, numero, Torre, vaga):
        self.id = int(id)
        self.numero = str(numero)
        self.torre = Torre
        self.vaga = int(vaga)
        self.proximo = None
    
    def imprimir(self):
        print(self.id, self.numero, self.torre, self.vaga, self.proximo)