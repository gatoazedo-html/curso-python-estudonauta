import math
adjacente = float(input('Digite o valor do cateto adjacente: '))
oposto = float(input('Digite o valor do cateto oposto: '))
hipotenusa = math.hypot(adjacente, oposto) #função para calcular a hipotenusa
print(f'a hipotenusa vai medir {hipotenusa:.2f}') #o :.2f so funciona no f string