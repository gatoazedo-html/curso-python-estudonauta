peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("alerta! abaixo do peso")
elif 18.5 <= imc <= 25:
    print("o peso ideal!")
elif 25 <= imc <= 30:
    print("alerta! sobrepeso")
elif 30 <= imc <= 40: #podia usar and aqui
    print("alerta! obesidade")
else:
    print("alerta! obesidade morbida")