from Computador import *
from Desktop import *
from Notebook import *

tela = Desktop('Hp','Branco', 1.500, 100)
print("----- Desktop -----")
print(tela.getInformacoes())
tela.modelo = 'AOC'
tela.cor = "Preto"
tela.preco = 1.000
print('Dados atualizados: ')
print(tela.getInformacoes())
tela.cadastrar()


print('\n----- Notebook -----')
note = Notebook('G3', 'Prata', 5.600, 500)
print(note.getInformacoes())
note.modelo = 'Acer'
note.cor = 'Prata'
note.preco = 2.000
print('Dados atualizados: ')
print(note.getInformacoes())
note.cadastrar()
