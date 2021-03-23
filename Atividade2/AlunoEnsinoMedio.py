from Aluno import *

class AlunoEnsinoMedio(Aluno):
    def __init__(self, cod, nome, matric, ano):
        self.ano = ano
        if self.ano == int(self.ano):
            Aluno.__init__(self, cod, nome, matric)

    def imprimirAno(self):
        try:
            if self.ano == int(self.ano):
                print(f"| Ano: {self.ano}",end=' ')
            else: 
                print()
                input('[ERRO] Campo ano somente números inteiros')
        except:
            input('No código informe apenas números')
        
 