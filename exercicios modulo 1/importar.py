import math #from math import sqrt se for so uma função
num = int(input('digite um numero inteiro: '))
raiz = math.sqrt(num)
print(f'a raiz quadrada de {num} é igual a {math.ceil(raiz)}') #arredondar pra cima ou floor para arredondar pra baixo
print(f'a raiz quadrada de {num} é igual a {raiz:.2f}')