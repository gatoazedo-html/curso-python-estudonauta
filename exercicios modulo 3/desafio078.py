valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(input(f'Digite um valor para a posição {cont}: '))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior: #valores[cont] significa o numero digitado
            maior = valores[cont] #ai se o valor digitado vira o maior, ele recebe o valor maior
        if valores[cont] < menor:
            menor = valores[cont]
print(valores)
print(f'o maior valor foi {maior} nas posições ', end='')
for pos, valor in enumerate(valores): #o enumerate ajuda aqui
    if valor == maior:
        print(f'{pos}...', end='')
print(f'\no menor valor foi {menor} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}...', end='')