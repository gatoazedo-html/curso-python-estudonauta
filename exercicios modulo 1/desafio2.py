n = int(input('digite um numero: '))
print(f'o numero digitado foi {n}')
print(f'o sucessor do numero {n} é {n+1} e o antecessor é {n-1} ')

n2 = int(input('digite um numero: '))
print(f'o numero digitado foi {n2}')
print(f'o dobro de {n2} é {n2*2}')
print(f'o triplo de {n2} é {n2*3}')
print(f'a raiz quadrada de {n2} é {n**(1/2):.2f}') #uma maneira boa de fazer a raiz quadrada

nota1 = float(input('digite a sua primeira nota: '))
nota2 = float(input('digite a sua segunda nota: '))
media = (nota1 + nota2)/2
print(f'a sua média é {media:.2f}') #maneira de deixar 2 pontos flutuantes apos a virgula

metros = float(input('digite a quantidade de metros: '))
cm = metros*100
mm = metros*1000
print(f'{metros} metros equivale a {cm} cm e {mm} mm')


