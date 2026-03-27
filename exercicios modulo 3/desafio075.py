tupla = (int(input('digite um numero: ')), int(input('digite outro numero: ')), int(input('digite outro numero: ')), int(input('digite outro numero: ')))
print(f'vc digitou: {tupla}')
print(f'o 9 apareceu : {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o primeiro 3 apareceu na {tupla.index(3)} posição')
else:
    print(f'não há o numero 3 na tupla')
print('os numeros pares são:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ') 