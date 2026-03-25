pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termos = 1
while termos <= 10:
    print(f'{pt} -> ', end='')
    pt += razao
    termos += 1
print('FIM')