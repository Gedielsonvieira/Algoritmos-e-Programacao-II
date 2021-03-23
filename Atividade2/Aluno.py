'''
    Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula. A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, que tem o atributo ano como seu atributo próprio e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. As duas subclasses herdam todos atributos da classe Aluno. As três classes possuem o método construtor e também o método imprimir, que imprime na tela os valores de todos os atributos da sua respectiva classe.  
'''

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        try:
            if codigo == int(codigo):
                self.imprimir()
            else:
                print() 
                input('[ERRO] Campo código somente números inteiros')
        except:
            input('No código informe apenas números')
    
    def imprimir(self):
        codigostr = 'Código:' 
        if codigostr.count('Código:'):
            print()
        print(f'{codigostr} {self.codigo} | Nome: {self.nome} | Matricula: {self.matricula}', end=' ')
        
        

