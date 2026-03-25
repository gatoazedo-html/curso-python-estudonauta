from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'temos {maior} pessoas maiores de idade e {menor} pessoas menores de idade')
