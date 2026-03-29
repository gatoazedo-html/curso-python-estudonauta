cadastro = {}
nome = []
sexo = []
idade = []
while True:
    nome.append(input('nome: '))
    cadastro['nome'] = nome
    sexo.append(input('sexo: [M/F] ').strip().upper()[0])
    while sexo[-1] not in 'MF':
        sexo.pop() #remove o último elemento da lista sexo, que é o sexo inválido que o usuário digitou
        print('sexo inválido, digite novamente.')
        sexo.append(input('sexo: [M/F] ').strip().upper()[0])
    cadastro['sexo'] = sexo
    idade.append(int(input('idade: ')))
    cadastro['idade'] = idade
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = input('deseja continuar? [S/N] ').strip().upper()[0]
    if confirmar == 'N':
        print('finalizando...')
        #cadastro.clear
        break
print('-='*30)
print(cadastro)
cadastro['total'] = len(cadastro['nome'])
print(f'foram cadastradas {cadastro["total"]} pessoas.')
media = sum(cadastro['idade']) / cadastro['total']
print(f'a média de idade é de {media:.2f} anos.')
print('as mulheres cadastradas foram: ', end='')
for i, v in enumerate(cadastro['sexo']):
    if v == 'F':
        print(cadastro['nome'][i], end=' ')
print('\nlistagem de pessoas com idade acima da média: ')
for i, v in enumerate(cadastro['idade']):
    if v > media:
        print(f'  - {cadastro["nome"][i]}: {v} anos')