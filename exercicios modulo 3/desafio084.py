pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: '))) #dados é temporario
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:]) #pessoas é a lista principal
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print(f'Temos {len(pessoas)} pessoas cadastradas.') #tamanho da lista pessoas
        for index, pessoa in enumerate(pessoas):
            if index == 0:
                maior = menor = pessoa[1] #pessoa[1] é o peso, pessoa[0] é o nome
            else:
                if pessoa[1] > maior:
                    maior = pessoa[1]
                if pessoa[1] < menor:
                    menor = pessoa[1]
        print(f'O maior peso foi de {maior}kg. Peso de ', end='')
        for pessoa in pessoas:
            if pessoa[1] == maior:
                print(f'[{pessoa[0]}] ', end='')
        print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
        for pessoa in pessoas:
            if pessoa[1] == menor:
                print(f'[{pessoa[0]}] ', end='')
        break