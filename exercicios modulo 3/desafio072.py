numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('digite um numero inteiro entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('tente novamente. digite um numero inteiro de 0 a 20: '))
print(numeros[n])
