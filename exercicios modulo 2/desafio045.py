#jokenpo v1.0
from random import randint
print('=' * 10 , 'jokenpô' , '=' * 10)
print('1 para tesoura')
print('2 para pedra')
print('3 para papel')

jogadaj1 = int(input('Qual a sua jogada? (1, 2 ou 3): '))
jogadapc = randint(1, 3)

if jogadaj1 == jogadapc:
    print('Empate!')
elif jogadaj1 == 1 and jogadapc == 2:
    print('jogador: tesoura')
    print('pc: pedra')
    print('pc ganhou!')
elif jogadaj1 == 1 and jogadapc == 3:
    print('jogador: tesoura')
    print('pc: papel')
    print('jogador ganhou!')
elif jogadaj1 == 2 and jogadapc == 3:
    print('jogador: pedra')
    print('pc: papel')
    print('pc ganhou!')
elif jogadaj1 == 3 and jogadapc == 2:
    print('jogador: papel')
    print('pc: pedra')
    print('jogador ganhou!')