n1=int(input('Digite o numero: '))
n2=int(input('Digite o numero: '))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
n3=int(input('Digite o numero: '))
if n3> maior:
    maior = n3
if n3<menor:
    menor=n3
print('O maior numero foi {}' .format(maior))
print('O menor numero foi {}' .format(menor))