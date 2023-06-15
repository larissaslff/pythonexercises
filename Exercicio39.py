import datetime
from datetime import date
ano_atual = date.today().year
nascimento=int(input('Em que ano nasceu? '))
idade = ano_atual - nascimento
if idade < 18:
    print('Ainda vai se alistar, faltam {} anos' .format(18 - idade))
elif idade > 18:
    print('Já passou da hora de alistar: {}' .format(idade -18))
else:
    print('Hora de se alistar')