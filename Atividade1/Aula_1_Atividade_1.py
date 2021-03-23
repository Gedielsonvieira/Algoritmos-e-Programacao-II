'''
    Construir um algoritmo que contenha 3 listas
        * Nomes dos produtos
        * Preços de cada produto
        * Quantidade de cada produto
    Construir uma função para imprimir um dos produtos das listas e uma função para retirar um dos produtos das listas
'''
from random import choice

nameProducts = ['Pepsi','Coca-Cola','Fruki','Sprite']
productsPrice = ['9','10','8','5']
amount = ['2','7','12','6']


def imprimiLinha():
    print('=-=-=-='*10)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def imprimir_nome_produto(lista1, lista2, lista3):
    indice = lista1.index(choice(lista1))
    print(f'Produtos escolhidos para impressão: \nNome do produto: {lista1[indice]} Preço: R${float(lista2[indice])} Quantidade: {lista3[indice]}')
    imprimiLinha()

imprimir_nome_produto(nameProducts, productsPrice, amount)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def remover_produto(lista1, lista2, lista3):
    indexList = lista1.index(choice(lista1))

    removePoductList1 = lista1.pop(indexList)
    removePoductList2 = float(lista2.pop(indexList))
    removePoductList3 = lista3.pop(indexList)
    print(f'Itens removidos: \nProduto: {removePoductList1} Preço: {removePoductList2} Quantidade: {removePoductList3}')
    imprimiLinha()
    print(f'Listas após remoção de itens: \n{lista1} \n{lista2} \n{lista3}')

remover_produto(nameProducts, productsPrice, amount)