km = int(input('qual a velocidade do carro? '))
if km > 80:
    print('MULTADO!')
    multa = (km - 80) * 7 #boa solução aqui
    print(f'a sua multa é de R${multa}')
else:
    print('dirija com segurança!')