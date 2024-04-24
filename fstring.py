"""Formatação básica de string
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex.: 0>-100,1f
conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')