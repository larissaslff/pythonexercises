maior = 0
menor = -1
for n in range(1, 6):
    peso = float(input('Digite o peso da pessoa nº {}: ' .format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} e o menor foi {}' .format(maior, menor))