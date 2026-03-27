alunos = []
while True:
    nome = input('nome: ')
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print('-=' * 30)
        print('Boletim'.center(60))
        print('-=' * 30)
        print('NUMERO - NOME: MÉDIA')
        for i, aluno in enumerate(alunos): #enumerate para mostrar o índice do aluno
            #index é o número do aluno, aluno[0] é o nome, aluno[1] são as notas, aluno[2] é a média
            print(f'{i} - {aluno[0]}: {aluno[2]}')
        pergunta = int(input('Mostrar notas de qual aluno? (999 para parar) '))
        while pergunta != 999:
            if pergunta < len(alunos):
                print(f'Notas de {alunos[pergunta][0]} são {alunos[pergunta][1]}')
            else:
                print('Aluno não encontrado.')
            pergunta = int(input('Mostrar notas de qual aluno? (999 para parar) '))
        print('Finalizando...')
        break