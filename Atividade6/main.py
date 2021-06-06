from No import *
from Pilha import *

pilha = Pilha()

print(f'Tamanho da lista: {len(pilha)}')


print(pilha)

pilha.inserir(4)
pilha.inserir(9)
pilha.inserir(265)
pilha.inserir(24)

print(pilha)

print(f"Item no topo: {pilha.verTopo()}")

print(f'Item Removido: {pilha.remover()}')