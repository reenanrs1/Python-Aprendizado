print('Calculadora de IMC Simples')
nome = input('Digite seu Nome: ')
altura = input('Digite sua Altura: ')
altura = float(altura)
peso = input('Digite seu Peso: ')
peso = float(peso)
imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'kg e seu imc é', imc)

if imc >=18.50 and imc <= 25:
    print('Seu peso IMC está normal')

elif imc > 25 and imc <= 29.99:
    print('Pré-Obesidade')
elif imc > 30 and imc <= 35:
    print('Obesidade Grau I')
elif imc > 35 and imc <= 40 :
    print('Obesidade Grau II.')