matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # matriz 3x3 para armazenar os valores digitados pelo usuário
for l in range(0, 3): # loop para percorrer as linhas da matriz
    for c in range(0, 3): # loop para percorrer as colunas da matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # solicita ao usuário que digite um valor para cada posição da matriz
print('Matriz preenchida:')
for l in range(0, 3): #para formatar a matriz de forma organizada
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # quebra de linha após cada linha da matriz

#SOMA DOS VALORES PARES ==================================================================
print(f'a soma de todos os valores pares é: ', end='') # para mostrar a soma dos valores pares
soma_pares = 0 # variável para armazenar a soma dos valores pares
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0: # verifica se o valor é par
            soma_pares += matriz[l][c] # adiciona o valor à soma dos pares
print(soma_pares) # mostra a soma dos valores pares

#SOMA DOS VALORES DA TERCEIRA COLUNA======================================================
soma_terceira_coluna = 0 # variável para armazenar a soma dos valores da terceira coluna
for l in range(0, 3):
    soma_terceira_coluna += matriz[l][2] # adiciona o valor da terceira coluna à soma
print(f'a soma dos valores da terceira coluna é: {soma_terceira_coluna}') # mostra a soma dos valores da terceira coluna

#MAIOR VALOR DA SEGUNDA LINHA=============================================================
maior_valor_segunda_linha = matriz[1][0] # inicializa o maior valor da segunda linha com o primeiro elemento da linha
for c in range(1, 3): # loop para percorrer os elementos da segunda linha
    if matriz[1][c] > maior_valor_segunda_linha: # verifica se o valor atual é maior que o maior valor encontrado até agora
        maior_valor_segunda_linha = matriz[1][c] # atualiza o maior valor da segunda linha
print(f'o maior valor da segunda linha é: {maior_valor_segunda_linha}') # mostra o maior valor da segunda linha