import random
def sorteia(valores):
    for i in range(0,5):
        valores.append(random.randint(0,10))
    print(f'Sorteando 5 valores da lista {valores}')

def somaPar(valores):
    soma = 0
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'a soma dos numeros pares é {soma}')


#programa principal
valores = []
sorteia(valores)
somaPar(valores)