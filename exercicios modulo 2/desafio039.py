from datetime import date
ano = int(input('digite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print(f'você ainda vai se alistar ao serviço militar. Faltam {18-idade} anos para o alistamento')
    print(f'você irá se alistar em {ano + 18}')
elif idade == 18:
    print('ja esta na hora de se alistar')
else:
    print(f'ja passou da hora de se alistar. Você está {idade-18} anos atrasado')
    print(f'você deveria ter se alistado em {ano+18}')