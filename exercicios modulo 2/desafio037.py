print("digite 1 para binário")
print("digite 2 para octal")
print("digite 3 para hexadecimal")
opcao = int(input('escolha qual conversão deseja realizar: '))
numero = int(input('digite um numero inteiro qualquer: '))

if opcao == 1:
    binario = bin(numero)[2:]
    print(binario)
elif opcao == 2:
    octal = oct(numero)[2:]
    print(octal)
elif opcao == 3:
    hexadecimal = hex(numero)[2:]
    print(hexadecimal)
else:
    print('opcao invalida. tente novamente')