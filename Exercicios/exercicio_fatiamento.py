"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não espaços)
        Seu nome tem {n} Letras
        a primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpe, você digitou campos vazios.
        """
nome = input('Digite seu primeiro nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é:{nome[::-1]}')  
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0:1:]}')
    print(f'A Ultima letra do seu nome é: {nome[-1::]}')
else:
    print('Desculpe, você digitou campos vazios')