dias = int(input('Quantos dia de aluguel? '))
km = int(input('Quantos km percorridos? '))
aluguel = (dias * 60) + (km * 0.15)
print('O valor do aluguel é {:.2f}'.format(aluguel))
