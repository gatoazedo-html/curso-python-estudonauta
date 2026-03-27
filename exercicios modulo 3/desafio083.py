expressao = input('digite sua expressao: ')
if expressao.count('(') == expressao.count(')'):
    print('sua expressao é valida')
else:
    print('sua expressao é invalida')


'''
expressao = input('digite sua expressao: ')
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressao é valida')
else:
    print('sua expressao é invalida')
'''
