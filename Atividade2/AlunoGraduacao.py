from Aluno import *

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        self.semestre = semestre
        if self.semestre == int(self.semestre):
            Aluno.__init__(self, codigo, nome, matricula)

    def imprimirSemestre(self):
        try:
            if self.semestre == int(self.semestre):
                print(f'| Semestre: {self.semestre}')
            else: 
                print()
                input('[ERRO] Campo semestre somente números inteiros')
        except:
            input('No código informe apenas números')
        

