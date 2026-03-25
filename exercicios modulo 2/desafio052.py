num = int(input('Digite um numero: '))
for c in range(2, int(num/2) + 1):
    if num % c == 0:
        print('n é primo')
        break
else:
    print('é primo')