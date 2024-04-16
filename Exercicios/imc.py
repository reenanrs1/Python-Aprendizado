print('Calculadora de IMC Simples')
nome = input('Digite seu Nome: ')
altura = input('Digite sua Altura: ')
altura = float(altura)
peso = input('Digite seu Peso: ')
peso = float(peso)
imc = peso / (altura ** 2)

linha =f'{nome} tem {altura:.2f} de altura e pesa {peso} kg e seu imc é {imc:.2f}'
print(linha) 

if imc >=18.50 and imc <= 25:
    print('Seu peso IMC está normal')
elif imc > 25 and imc <= 29.99:
    print('Pré-Obesidade')
elif imc > 30 and imc <= 34.99:
    print('Obesidade Grau I')
elif imc > 35 and imc <= 40 :
    print('Obesidade Grau II.')