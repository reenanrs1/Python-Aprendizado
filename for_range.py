"""
For + Range
range -> range( start, stop, step)
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador.
"""

# numeros = range(0, 10, 2)

# for numero in numeros:
#     print(numero)

# texto = "Renan" #iterável
# iteratador = iter(texto) #iterador

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break
# print('#####################Que é a mesma coisa que: ')
# ##### que é a mesma coisa que
# for letra in texto:
#     print(letra)

for i in range(10):
     if i == 2:
        print("i é 2, pulando...")
        continue
    #  if i == 8:
    #      print("i é 8, seu else não executar")
    #      break
     for j in range (1,3):
         print(i,j)
else:
    print("For completo com sucesso!!!")
        