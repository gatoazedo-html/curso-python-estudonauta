lista_idade = []
lista_nomes = []
lista_mulheres = []

for i in range(1, 3):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('[M] - para Masculino e [F] para Feminino: ')).upper()
    lista_idade.append(idade)
    lista_nomes.append(nome)
    if sexo == 'F' and idade < 20:
        lista_mulheres.append(nome)

mais_velho = max(lista_idade)
indice_mais_velho = lista_idade.index(mais_velho)

print(f'A média de idade é de {sum(lista_idade) / len(lista_idade)} anos')
print(f'O HOMEM mais velho é o {lista_nomes[indice_mais_velho]} e ele tem {max(lista_idade)} anos')
print(f'Ao total são {len(lista_mulheres)} que tem menos de 20 anos')