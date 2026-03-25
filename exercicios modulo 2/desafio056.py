soma = 0
mulher_menor = 0
nome_maior = 0
idade_maior = -1
for c in range(1, 5):
    nome = input('digite seu NOME: ')
    idade = int(input('digite sua IDADE: '))
    sexo = input('digite seu SEXO: ').upper()
    print('')
    soma += idade
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    if sexo == 'M':
        if idade > idade_maior:
            idade_maior = idade
            nome_maior = nome
print(f'a media das idades foi {soma/4}')
print(f'o homem mais velho foi {nome_maior}')
print(f'temos {mulher_menor} mulheres menores de 20 anos')
