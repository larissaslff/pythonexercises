from random import randint
numeros = (randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10)
           )
print(f'Os valores sorteados ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi {max(numeros)}', end=' ')
print(f'e o menor valor foi {min(numeros)}')
