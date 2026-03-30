from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nanalisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nforam informados {cont} valores e o maior é {maior}')





#programa principal
maior(2,8,1,4)
maior(4,7,0)