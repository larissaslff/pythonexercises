cont = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        cont +=1
if c > 1:
    print('O nº {} foi divisível {} vezes' .format(num, cont))
else:
    print('O nº {} foi divisível {} vez'.format(num, cont))
if cont == 2:
    print('É primo')
else:
    print('Não é primo')