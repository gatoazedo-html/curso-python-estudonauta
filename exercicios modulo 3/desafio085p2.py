num = [[], []]  # lista para armazenar números pares e ímpares
valor = 0 # variável para receber o valor digitado pelo usuário
for c in range(1, 8):
    valor = int(input('digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor) # adiciona o valor na lista de números pares
    else:
        num[1].append(valor) #adiciona o valor na lista de numeros impares
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')