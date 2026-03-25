km = int(input('qual a distancia da viagem? '))
if km <= 200:
    print(f'a viagem custa {km * 0.50} reais')
else:
    print(f'a viagem custa {km * 0.45} reais')