num = int(input('digite um numero de 0 a 9999: '))
while num < 1000 or num > 9999:
    num = int(input('digite um numero de 0 a 9999: '))
num = str(num)
#talvez esse modo com print nao seja o melhor
print(f'unidade: {num[3]}')
print(f'dezena: {num[2]}')
print(f'centena: {num[1]}')
print(f'milhar: {num[0]}')

'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
'''