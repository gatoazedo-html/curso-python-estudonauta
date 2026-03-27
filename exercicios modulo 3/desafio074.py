import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'os valores sorteados: {tupla}')
print(f'o maior numero gerado: {sorted(tupla)[-1]}') #poderia usar max e min
print(f'o menor numero gerado: {sorted(tupla)[0]}')