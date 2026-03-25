teste = float(input('digite a nota do teste: '))
prova = float(input('digite a nota do prova: '))
media = (teste + prova) / 2
if media < 5.0:
    print('reprovado')
elif 5.0 <= media <= 6.9: #podia usar and aqui
    print('recuperação')
else:
    print('aprovado')