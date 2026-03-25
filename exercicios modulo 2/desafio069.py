maioridade = homens = mulheres_menor = 0
while True:
    print('-'*10)
    idade = int(input('digite sua idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o seu sexo: [M/F] ').upper()
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            mulheres_menor += 1
    print('cadastro concluido')
    print('-'*10)
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = input('Deseja continuar? [S/N] ').upper()
    if confirmar == 'N':
        break
print('-'*10)
print(f'foram cadastradas {maioridade} pessoas maiores de 18 anos')
print(f'foram cadastrados {homens} homens')
print(f'foram cadastradas {mulheres_menor} mulheres com menos de 20 anos')
print('-'*10)
print('encerrando...')