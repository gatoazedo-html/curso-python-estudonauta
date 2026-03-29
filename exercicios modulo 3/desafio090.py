aluno = {}
aluno['nome'] = input('nome: ')
aluno['média'] = float(input('média: '))
print(f'o nome do aluno é {aluno["nome"]}')
print(f'a média de aluno é {aluno["média"]}')
if aluno['média'] >= 6:
    aluno['situação'] = 'aprovado'
    print(f'a situação do aluno é {aluno["situação"]}')
else:
    aluno['situação'] = 'reprovado'
    print(f'a situação do aluno é {aluno["situação"]}')
print(aluno)