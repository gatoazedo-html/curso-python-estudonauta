sexo = input('Digite o sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F': #sexo not in 'MmFf'
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso')