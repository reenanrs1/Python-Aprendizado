"""
Flag(Bandeira) - Marcar um local
Nome = Não valor
Is e IS not = é ou não  e (tipo, valor, identidade)
id = identidade
"""



condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no IF')