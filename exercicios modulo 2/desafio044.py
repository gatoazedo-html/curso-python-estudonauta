preco = int(input('digite o valor do produto: '))
print("1 para pagamento a vista no dinheiro/pix")
print("2 para pagamento a vista no cartão")
print("3 para pagamento em até 2x no cartão")
print("4 para pagamento em 3x ou mais no cartão")
forma_pag = int(input('digite sua forma de pagamento: '))
if forma_pag == 1:
    print(f'você pagará R${preco - (preco * 10 / 100):.2f}')
elif forma_pag == 2:
    print(f'você pagará R${preco - (preco * 5 / 100):.2f}')
elif forma_pag == 3:
    print(f'você pagará R${preco}, as parcelas ficarão em {preco/2:.2f}')
elif forma_pag == 4:
    parcela = int(input('digite sua parcela: '))
    print(f'você pagará R${preco + (preco * 0.20):.2f}. as parcelas ficarão em {preco/parcela:.2f}')
else:
    print('opção inválida! tente novamente')
