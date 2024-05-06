"""Calculadora com while"""



while True:
    print('##############Calculadora no Terminal com While################')
    numero1 = input('Digite o primeiro numero: ')
    operador = input('Digite o operador que deseja(+-/*):  ')
    numero2 = input('Digite o segundo numero: ')


    numeros_validos = None
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Numeros invalidos, digite novamente')
        continue
    if numeros_validos is True:
        if operador == '+':
            print(num_1_float + num_2_float)
        if operador == '-':
            print(num_1_float - num_2_float)
        if operador == '*':
            print(num_1_float * num_2_float)
        if operador == '/':
            print(num_1_float / num_2_float)


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    

    if sair is True:
        break