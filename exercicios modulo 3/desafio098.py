from time import sleep
def contador (i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += p
        print()
        print('=' * 30)
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= p
        print()
        print('=' * 30)



#programa principal
contador(0, 100, 10)
contador(10, 0, 2)
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo)

