#verificando indices
# nome = 'Renan'
# print(nome[2])

# nome = 'Renan'
# print('n' in nome)
# print(10 * '-')
# print('n' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
