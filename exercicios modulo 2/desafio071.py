valor = int(input('que valor você quer sacar:'))
cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0
while valor != 0:
    if valor >= 50:
        valor -= 50
        cedula_50 += 1
    elif valor >= 20:
        valor -= 20
        cedula_20 += 1
    elif valor >= 10:
        valor -= 10
        cedula_10 += 1
    else:
        valor -= 1
        cedula_1 += 1
print(f'voce precisou de {cedula_50} cedulas de 50 reais')
print(f'voce precisou de {cedula_20} cedulas de 20 reais')
print(f'voce precisou de {cedula_10} cedulas de 10 reais')
print(f'voce precisou de {cedula_1} cedulas de 1 reais')
