sal = float(input('Qual o seu salario: '))
if sal > 1250:
    novo = sal + (sal * 10 / 100)
    print(f'o seu salario foi de R${novo:.2f}')
else:
    novo = sal + (sal * 15 / 100)
    print(f'o seu salario foi de R${novo:.2f}')