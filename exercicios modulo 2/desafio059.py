n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

while True:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair')
    opcao = int(input('Digite uma opcao: '))
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}\n')
    elif opcao == 2:
        print(f'{n1} * {n2} = {n1 * n2}\n')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} > {n2}\n')
        elif n1 < n2 :
            print(f'{n1} < {n2}\n')
        else:
            print(f'{n1} = {n2}\n')
    elif opcao == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: \n'))
    elif opcao == 5:
        print('encerrando programa...')
        break
    else:
        print('Opcao invalida. tente novamente\n')