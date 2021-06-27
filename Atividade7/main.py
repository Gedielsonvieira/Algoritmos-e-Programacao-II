from Torre import *
from Apartamento import *
from Garagem import *


print("Apartamentos: ")
apt1 = Torre(1, "Torre 1", "Florida")
apt2 = Torre(2, "Torre 2", "rua x")

apt1.imprimir()
apt2.imprimir()
#=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("\nGaragem: ")
garagem = Garagem()
garagem.imprimir()
print(len(garagem))
#=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("=-"*30)
garagem.inserir(10, "1010", apt1, 1)
garagem.imprimir()
print(len(garagem))

print("=-"*30)
garagem.remover()
garagem.imprimir()
#=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("=-"*30)
garagem.inserir(20, "2020", apt2, 3)
garagem.imprimir()
print(len(garagem))

print("=-"*30)
garagem.remover()
garagem.imprimir()

