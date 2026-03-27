tupla = ('aprender', 'programar', 'linguagem', 'python',)

for palavra in tupla:
    print(f'\nna palavra {palavra.upper()} temos ', end='')
    for letra in palavra: #usar um laço dentro do outro
        if letra.lower() in 'aeiou':
            print(letra, end=' ')