a = float(input('Digite o valor da linha a: '))
b = float(input('Digite o valor da linha b: '))
c = float(input('Digite o valor da linha c: '))
if a < b + c and b < a + c and c < a + b:
    print('é um triangulo!!')
else:
    print('triangulo inválido!')
print('encerrando programa...')