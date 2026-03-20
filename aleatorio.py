'''
import random
alunos = ['natalia', 'patricia', 'lidia', 'yona']
sorteio = random.choice(alunos)
print(sorteio)
'''

#Percebi que poderia fazer melhor com o laço de repetição

import random
alunos = []
while True:
    aluno = input('Digite o nome do aluno: ')
    if aluno.lower() == 'sair':
        print(alunos)
        print(f'o aluno sorteado foi {random.choice(alunos)}')
        break
    alunos.append(aluno) #deixar fora pq senao vai acrescentar o 'sair' na lista