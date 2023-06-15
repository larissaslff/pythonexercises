produtos = ('Canteta', 1, 'Caderno', 25,"Arroz", 20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
cont = 0
while cont < len(produtos) -1:
   print(f'{produtos[cont]:.<30}'
         f' R${produtos[cont +1]:>5.2f}')
   cont +=2
print('-' * 40)