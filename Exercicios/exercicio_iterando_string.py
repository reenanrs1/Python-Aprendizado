"""
Iterando string com while
"""

# 01234567891
nome = 'Renan Victor'


indice = 0
novo_nome = ''
while indice < len(nome):
    
    letra = nome[indice]
    novo_nome += letra + '*'
    indice += 1

print(novo_nome)