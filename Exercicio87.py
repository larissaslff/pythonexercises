matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = somacoluna3 =0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor {l,c}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz[l][2]:
            somacoluna3 += matriz[l][2]
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()
print(f'A soma dos pares é {pares}')
print(f'A soma dos valores da 3ª coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')