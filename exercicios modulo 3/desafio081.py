valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if confirmar == 'N':
        print(f'vc digitou {len(valores)} elementos')
        valores.sort(reverse=True) #n dá pra colocar dentro do print
        print(valores)
        if 5 in valores:
            print(f'O valor 5 faz parte da lista')
        else:
            print('o 5 não está na lista')
        break