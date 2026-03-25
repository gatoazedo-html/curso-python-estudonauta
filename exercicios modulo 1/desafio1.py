#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

caractere = (input('Digite uma caractere: '))
print(f'o caractere digitado é {caractere}')
print(f'o caractere digitado é do tipo {type(caractere)}')
print(f'o caractere é um número: {caractere.isnumeric()}')
print(f'o caractere é uma palavra: {caractere.isalpha()}')
print(f'o caractere contem uma palavra ou número (alfanumerico): {caractere.isalnum()}')
print(f'o caractere esta com letras minusculas: {caractere.islower()}')
print(f'o caractere esta com letras maiusculas: {caractere.isupper()}')
print(f'o caractere esta capitalizada (maiusculas e minusculas): {caractere.istitle()}')
print(f'o caractere esta vazio: {caractere.isspace()}')
