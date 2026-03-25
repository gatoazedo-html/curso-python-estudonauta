import random
from time import sleep #biblioteca time
print('-'*33)
print('pensando em um numero de 0 a 5...')
print('-'*33)
num = random.randint(0,5)
adv = int(input('tente advinhar o numero escolhido pelo computador: '))
print('processando...')
sleep(1)
if num == adv:
    print('você acertou!')
else:
    print(f'você errou! O numero escolhido foi {num}. Computador venceu!')
print('encerrando programa...')