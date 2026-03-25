from datetime import date
ano = int(input('qual o ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print('categoria: MIRIM')
elif idade <= 14:
    print('categoria: INFANTIL')
elif idade <= 19:
    print('categoria: JUNIOR')
elif idade <= 25:
    print('categoria: SENIOR')
else:
    print('categoria: MASTER')
