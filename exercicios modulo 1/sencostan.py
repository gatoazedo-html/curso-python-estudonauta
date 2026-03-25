import math
angulo = float(input('Digite o valor do angulo: '))
cosseno = math.cos(math.radians(angulo)) #faltou o math.radians
tangente = math.tan(math.radians(angulo))
seno = math.sin(math.radians(angulo))
print(f'o seno de {angulo} é {seno:.2f}.\no cosseno é {cosseno:.2f}.\na tangente é {tangente:.2f}')
