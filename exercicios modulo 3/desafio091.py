from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    sleep(0.5)
    print(f'o {k} tirou {v}')
print('Ranking dos jogadores: ')
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True) #entender depois esse key=lambda item: item[1] - ordena pelo valor do dado, e não pela chave do jogador
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
