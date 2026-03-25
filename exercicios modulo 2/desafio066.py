s = c = 0
while True:
    n = int(input('digite um numero (digite 999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'vc digitou {c} numeros e a soma entre eles é {s}')