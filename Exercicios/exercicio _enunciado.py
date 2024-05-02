"""
Faça um programa que peça ao usuário para digitar um número inteiro.
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um numero inteiro
"""
numero = input('Digite um numero inteiro: ')

try:
    numero = int(numero)
    # If conversion is successful, proceed to check if it's even or odd
    if numero % 2 == 0:
        print('O numero é par')
    else:
        print('O numero é ímpar')
except ValueError:
    # If conversion fails, it means the input was not an integer
    print('O número não é inteiro')




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario descrito,
exiba a saudação apropriada.
Ex: Bom dia 00-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = int(input('Digite as horas'))
if hora < 12:
    print('Bom dia')
elif hora < 18:
    print('Boa tarde')
else:
    print('Boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')



