nome = input('digite seu nome: ').strip()
nome = nome.split()
print(f'primeiro nome: {nome[0]}')
print(f'ultimo nome: {nome[len(nome)-1]}')