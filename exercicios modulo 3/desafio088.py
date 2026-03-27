from random import randint
from time import sleep
lista = [] #lista temporaria
jogos = [] #lista definitiva
quant = int(input('Quantos jogos você quer que eu sorteie? ')) #quantidade de jogos
tot = 1 #contador de jogos
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
