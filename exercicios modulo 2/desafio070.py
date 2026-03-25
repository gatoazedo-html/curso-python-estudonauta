soma = produto_mil = nome_produto = mais_barato = cont = 0
produto_barato = ''
while True:
    nome_produto = input('Digite o nome do produto: ').upper()
    preco = float(input('qual o preço do produto: '))
    soma += preco
    cont += 1
    if cont == 1 or preco < mais_barato: #colocar o contador pro primeiro valor
        mais_barato = preco
        produto_barato = nome_produto
    elif preco > 1000:
        produto_mil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-'*10)
print(f'o total da compra foi R${soma}')
print(f'foram {produto_mil} produtos acima de mil reais')
print(f'o produto mais barato foi {produto_barato} e ele custa {mais_barato}')