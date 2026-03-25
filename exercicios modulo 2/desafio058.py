from random import randint
from time import sleep

print('=' * len('jogo da advinhação'))
print('jogo da advinhação')
print('=' * len('jogo da advinhação'))
print('pensando...')
sleep(1)
print('pensei em um numero!')

adv = randint(0,10)
tentativas = 1
numero = int(input('Digite um numero de 0 a 10: '))

while numero != adv:
    tentativas += 1
    print('errouu!')
    if numero < adv:
        print('mais...')
    else:
        print('menos...')
    numero = int(input('Digite um numero de 0 a 10: '))
print(f'Voce acertou! você precisou de {tentativas} tentativas')