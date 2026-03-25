casa = float(input('Qual o valor da casa? R$'))
sal = float(input('qual o seu salario? R$'))
anos = int(input('quantos anos deseja pagar? '))
meses = anos * 12
prestacao = casa / meses
limite = sal * 30/100
if prestacao > limite:
    print(f'Para pagar uma casa de R${casa} em {anos} a prestação será de R${prestacao:.2f}. o seu emprestimo foi negado')
else:
    print(f'Para pagar uma casa de R${casa} em {anos} a prestação será de R${prestacao:.2f}. o seu emprestimo foi aprovado')