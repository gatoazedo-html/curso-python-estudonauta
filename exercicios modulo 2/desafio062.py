pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termos = 1
while termos <= 10:
    print(f'{pt} -> ', end='')
    pt += razao
    termos += 1
    if termos > 10:
        while True:
            pergunta = input('Deseja continuar? [S/N] ? ').upper()
            if pergunta == 'S':
                pt += razao
                print(f'{pt} -> ', end='')
                termos += 1
            else:
                print('encerrando programa...')
                break