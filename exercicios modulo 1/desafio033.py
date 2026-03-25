num = []
i = 0
while i < 3:
    n = int(input('digite um numero: '))
    num.append(n)
    i += 1
num.sort()
print(f'o menor numero digitado foi {num[0]} e o maior foi {num[-1]}')