frase = input('Digite uma frase: ').lower().replace(' ', '')
inverso = frase[::-1]
if frase == inverso:
    print('Palindromo')
else:
    print('nao é palindromo')
