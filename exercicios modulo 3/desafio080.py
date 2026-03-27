valores = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[-1]: #valores[-1] significa o ultimo numero
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0 # serve como index
        while pos < len(valores):
            if valor <= valores[pos]: #pos vira aqui o indice para representar a posição dos numeros
                valores.insert(pos, valor) #insere valor na posição pos
                print(f'adicionado na posição {pos} da lista')
                break
            pos += 1 #incremento do pos se n é loop infinito
print(valores)