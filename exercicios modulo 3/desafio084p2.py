temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0: #significa o inicio da lista, entao o primeiro peso é o maior e o menor
        maior = menor = temp[1] #temp[1] é o peso, temp[0] é o nome
    else:
        if temp[1] > maior:  #comparando o peso colocado com o maior peso atual
            maior = temp[1] #ai acrescenta aqui o novo peso
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'ao todo, voce cadastrou {len(princ)} pessoas')
print(f'o maior peso foi de {maior}kg. peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print() #quebra de linha
print(f'o menor peso foi de {menor}kg. peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
print('encerrando...')