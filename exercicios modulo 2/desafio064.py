c = soma = num = 0
num = int(input('digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('digite um numero [999 para parar]: '))
    if num == 999:
        break
print(f'você digitou {c} numeros e a soma entre eles é {soma}')
