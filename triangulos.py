a = int(input('digite o lado a do triangulo: '))
b = int(input('digite o lado b: '))
c = int(input('digite o lado c: '))

while not (a < b + c and b < a + c and c < a + b):
    print('triangulo inválido. Tente novamente')
    a = int(input('digite o lado a do triangulo: '))
    b = int(input('digite o lado b: '))
    c = int(input('digite o lado c: '))

if a == b == c:
    print('triangulo equilatero')
elif a == b or a == c or b == c:
    print('triangulo isosceles')
else:
    print('triangulo isosceles')
