import random
print('pensando em um numero de 0 a 5...')
num = random.randint(0,5)
adv = int(input('tente advinhar o numero escolhido pelo computador: '))
if num == adv:
    print('você acertou!')
else:
    print(f'você errou! O numero escolhido foi {num}. Computador venceu!')
print('encerrando programa...')