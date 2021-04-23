from ContaCorrente import *
from ContaPoupanca import * 

print('Conta Corrente')
c = ContaCorrente(123, 165165, 16516516, 'nu')
c.cadastrar()
c.depositar = 1000
print(c.saldo,'\n')

#--------------------------------------------------

print('Conta Poupança')
p = ContaPoupanca('Arnaldo', 121, 'Sicredi')
p.cadastrar()
p.depositar = 100
print(p.saldo)