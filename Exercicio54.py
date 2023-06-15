from datetime import date
menor =0
maior =0
ano_atual = date.today().year
for n in range(1, 8):
    ano_nasc=int(input('Em que ano a {}ª pessoa nasceu? ' .format(n)))
    if ano_atual - ano_nasc < 21:
        menor += 1
    else:
        maior += 1
print('Há {} maiores e {} menores' .format(maior, menor))
