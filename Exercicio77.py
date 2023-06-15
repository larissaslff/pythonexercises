palavras = ('melissa', 'ana', 'bola', 'girafa', 'cachorro', 'futuro')

# for i in palavras:
#     print(f'\nNa palavra {i.upper()} temos ', end= '')
#     if i.count('a') > 0:
#         print('a', end= ' ')
#     if i.count('e') > 0:
#         print('e', end=' ')
#     if i.count('i') > 0:
#         print('i', end=' ')
#     if i.count('o') > 0:
#         print('o', end=' ')
#     if i.count('u') > 0:
#         print('u', end=' ')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end =' ')
