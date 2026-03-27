valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print(valores)
        print(pares)
        print(impares)
        print('Encerando o programa...')
        break