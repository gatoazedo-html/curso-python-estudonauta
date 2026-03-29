time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    gols.clear()
    jogador["nome"] = input('nome do jogador: ') #dicionario pra cada jogador
    pergunta = int(input(f'quantas partidas {jogador["nome"]} jogou? ')) #tot
    for c in range(0, pergunta):
        gols.append(int(input(f'quantos gols na partida {c+1}?: ')))
    jogador["gols"] = gols[:] #adiciona gols dentro do dicionario jogador
    jogador["total"] = sum(gols) #total de gols dentro do dicionario jogador
    time.append(jogador.copy()) #a lista time recebe o dicionario jogador
    while True:
        confirmar = str(input('quer continuar? [S/N] ')).upper().strip()[0]
        if confirmar in 'SN':
                break
        print('resposta inválida. Digite S ou N.')
    if confirmar == 'N':
         break

print('-='*30)
print(f'{"cod":>4} {"nome":<15} {"gols":<15} {"total":<15}')
for i, j in enumerate(time):
    print(f'{i:>4}', end=' ')
    for k in j.values():
        print(f'{str(k):<15}', end=' ')
    print()
print('-='*30)

while True:
    busca = int(input('mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999: #indice do jogador
        print('finalizando...')
        break
    if busca >= len(time):
        print(f'jogador com código {busca} não encontrado. Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, v in enumerate(time[busca]["gols"]): #enumerate para pegar o indice e outro dado
            print(f'   => na partida {i+1} fez {v} gols.')

