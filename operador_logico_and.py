#todas as condições devem ser verdadeira.

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrando no sistema')

else:
    print('Senha incorreta.')