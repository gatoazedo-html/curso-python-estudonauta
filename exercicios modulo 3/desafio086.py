matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # matriz 3x3 para armazenar os valores digitados pelo usuário
for l in range(0, 3): # loop para percorrer as linhas da matriz
    for c in range(0, 3): # loop para percorrer as colunas da matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # solicita ao usuário que digite um valor para cada posição da matriz
print('Matriz preenchida:')
for l in range(0, 3): #para formatar a matriz de forma organizada
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # quebra de linha após cada linha da matriz