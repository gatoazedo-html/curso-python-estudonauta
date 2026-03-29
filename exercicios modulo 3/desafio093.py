jogador = {}
jogador["nome"] = input('nome do jogador: ')
pergunta = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(0, pergunta):
    gols.append(int(input(f'quantos gols na partida {c+1}?: ')))
jogador["gols"] = gols #jogador["gols"] = gols.copy() #se usar copy, a lista gols pode ser modificada depois, e isso vai modificar a lista dentro do dicionário jogador, porque elas são o mesmo objeto na memória. Se usar copy, a lista dentro do dicionário jogador é uma cópia da lista gols, e não o mesmo objeto na memória.
jogador["total"] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem valor {v}.')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {pergunta} partidas.')
for i, v in enumerate(jogador["gols"]): #i é o indice da partida, v é a quantidade de gols na partida
    print(f'   => na partida {i+1} fez {v} gols.')