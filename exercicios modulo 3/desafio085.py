valores = []
pares = []
impares = []
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    valores.append(valor)
    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    valores.clear()
print(f'Os valores pares são: {sorted(pares)}')
print(f'Os valores ímpares são: {sorted(impares)}')