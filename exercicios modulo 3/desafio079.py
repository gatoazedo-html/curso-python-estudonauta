valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('este valor ja esta na lista')
    else:
        valores.append(valor)
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if confirmar == 'N':
        print(sorted(valores))
        print('finalizando...')
        break