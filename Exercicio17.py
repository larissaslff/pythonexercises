from math import sqrt, pow
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = sqrt((pow(catetoOposto, 2)) + (pow(catetoAdjacente, 2)))
print('A hipotenusa do triangulo é {:.2f}' .format(hipotenusa))
