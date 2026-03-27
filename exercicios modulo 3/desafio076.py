listagem = ('pão', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #PARA DEIXAR CENTRALIZADO
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}R$', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
print('-'*40)