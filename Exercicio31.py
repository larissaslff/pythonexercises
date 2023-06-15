distancia=float(input('Qual a distancia? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço da viagem é R$ {:.2f}' .format(preco))