s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'o somatorio de todos os {cont} numeros impares multiplos de 3 de 1 a 500 foi {s}')
print('fim')