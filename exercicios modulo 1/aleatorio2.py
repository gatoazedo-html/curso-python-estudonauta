'''
import random
alunos = ['natalia', 'patricia', 'lidia', 'yona']
random.shuffle(alunos) #n pode colocar variavel aqui!!
print(alunos)

'''

import random
alunos = []
while True:
    aluno = input('Digite o nome do aluno: ')
    if aluno.lower() == 'sair':
        random.shuffle(alunos)
        print(f'a ordem de apresentação será {alunos}')
        break
    alunos.append(aluno) #lista.append(item)