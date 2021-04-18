from Pessoa import *
from Fisica import *
from Juridica import *


p = Pessoa(1, 'Luana', 'Porto Alegre', 9165136106)
p.imprimeNome()
p._Pessoa__imprimeTelefone()

#=-=-=--=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('''
--- Pessoa Física ---''')
pf = Fisica(2, 'Luiz', 'avenida', 9999999, 934163410, 20, 64, 1.70 )
print(pf.nome)
print(f'Código: {pf._Pessoa__codigo}')
pf.imprimeCPF()
pf._Fisica__calculaIMC()

#=-=-=--=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('''
--- Pessoa Jurídica ---''')
pj = Juridica(3, 'Gerso', 'Avenida Castelo Branco', 9999999, 934163410, 'codebal', 64)
pj._Juridica__emitirNotaFiscal()
