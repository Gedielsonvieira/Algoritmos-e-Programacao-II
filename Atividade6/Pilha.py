from No import *

class Pilha:
    def __init__(self):
        self.topo = None #endereço de memória
        self.tamanho = 0

    def inserir(self, elemento): # inserção apenas no topo
        # No rebece o dado então precisamos utilizar o No
        # o primeiro a chegar vai ser o topo
        no = No(elemento)
        # cada No conhece quem está logo abaixo na pilha, então o No que acabou de ser criado precisa ser ligado antigo topo
        no.proximo = self.topo
        # topo recebe o No que foi criado por último
        self.topo = no
        # após add na pilha aumentar tamanho da pilha 
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            # saber quem está no topo
            no = self.topo
            # mover o topo uma posição abaixo 
            self.topo = self.topo.proximo
            # após retirar algo da pilha reduzir tamanho da pilha 
            self.tamanho -= 1
            return no.dado
        else:
            print('Lista Vazia')

    def __len__(self):
        return self.tamanho

    def verTopo(self):
        if self.tamanho > 0:
            return self.topo.dado
        else:
            print('Lista Vazia')

    def __repr__(self):
        pilha = ''
        auxiliar = self.topo
        while(auxiliar):
            pilha += str(auxiliar.dado) + "\n"
            auxiliar = auxiliar.proximo
        return pilha
