pesos = []
for c in range(1, 6):
    peso = float(input('digite seu peso: '))
    pesos.append(peso)
pesos.sort()
print(f'o menor peso foi {pesos[0]} e o maior peso foi {pesos[-1]}')