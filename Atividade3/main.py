from Veiculo import *
from Automovel import *
from Bicicleta import *
from Moto import *
from Carro import *

patinete = Veiculo("fiat", 4, "uno")
patinete.imprimirInformacoes()

trem = Automovel('bmw',20,'trensurb',200,600)
trem.imprimirInformacoes()

bike = Bicicleta('caloi',2,'ride',80,18,True)
bike.imprimirInformacoes()

z300 = Moto('Kawasaki',2,'z300',180,300,True)
z300.imprimirInformacoes()

carro = Carro('Peugeot',4,'SUV-3008',220,1598,4)
carro.imprimirInformacoes()
carro.acelerar(10)
carro.frear(100)
carro.imprimirInformacoes()