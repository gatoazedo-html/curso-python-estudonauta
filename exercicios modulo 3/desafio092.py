import datetime
cadastro ={
    'nome': input('nome: '),
    'ano': int(input('ano de nascimento: ')),
    'ctps': int(input('carteira de trabalho (0 não tem): ')),
}
cadastro['idade'] = datetime.datetime.now().year - cadastro['ano']
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('ano de contratação: '))
    cadastro['salario'] = float(input('salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - cadastro['ano']
for k, v in cadastro.items():
    print(f'{k} tem valor {v}.')