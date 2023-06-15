from datetime import date

ano = date.today().year

nascimento = int(input('Em que ano nasceu? '))

idade = ano - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
else:
    print('MASTER')
