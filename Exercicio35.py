l1=int(input('Digite: '))
l2=int(input('Digite: '))
l3=int(input('Digite: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode ser triangulo')
else:
    print('Não forma triangulo')