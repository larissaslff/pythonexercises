numeros = []
for i in range(0, 5):
    n = int(input('Digite um valor? '))
    numeros.append(n)
    numeros.sort()
    if numeros.index(n) == len(numeros) -1:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {numeros.index(n)} da lista...')
print(f'Os valores adicionas em ordem foram {numeros}')