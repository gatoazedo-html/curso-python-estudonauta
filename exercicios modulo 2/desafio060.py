num = int(input('Digite um numero: '))
fat = 1 #variavel da fatorial e toda variavel de multiplicacao tem q comecar com 1
if num < 0:
    print('Não existe fatorial de numero negativo')
elif num == 0:
    print('O fatorial de 0 é 1')
else:
    original_num = num #para armazenar o valor original que se perde no loop
    while num > 0:
        fat *= num #lembrar do *=
        num -= 1 #decrementar a variavel
    print(f'O fatorial de {original_num}! é {fat}')

'''
n = int(input('Digite um numero: '))
c = n
f = 1
while c > 0:
    print(f'{c}' end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')
'''