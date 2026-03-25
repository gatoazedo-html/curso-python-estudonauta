nome = input('Qual o seu nome? ')
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(f'o primeiro nome tem {len(dividido[0])} letras') #nome.find(' ')
print(f'o nome tem {len(nome.replace(' ', ''))} letras') #len(nome) - nome.count(' ')


