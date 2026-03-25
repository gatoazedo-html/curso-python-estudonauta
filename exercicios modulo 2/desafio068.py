from random import randint
vitoria = 0
print('-' * 30)
print('Vamos jogar Par ou Impar')
print('-' * 30)
while True:
    n = int(input('digite um numero inteiro: '))
    pc = randint(0, 10)
    soma = pc + n
    par_impar = ' '
    while par_impar not in 'PpIi':
        par_impar = input('Par ou Impar? [P/I] ').upper()
    print(f'voce jogou {n} e o computador jogou {pc}. total de {soma}.')
    print('deu par' if soma % 2 == 0 else 'deu impar')
    if par_impar == 'P':
        if soma % 2 == 0:
            print('voce venceu!')
            vitoria += 1
        else:
            print('voce perdeu!')
            break
    elif par_impar == 'I':
        if soma % 2 != 0:
            print('voce venceu!')
            vitoria += 1
        else:
            print('voce perdeu!')
print(f'game over! Voce venceu {vitoria} vezes')