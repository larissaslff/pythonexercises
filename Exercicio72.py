ex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
      'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
      'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
      'dezenove', 'vinte')
valor = ' '
while True:
    while valor not in range(0, 21):
        valor = int(input('Digite um valor de 0 a 20: '))
    print(f'Você selecionou o número {ex[valor]}')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continar? [S/N]')).upper().strip()[0]
    if res == 'N':
        break
    else:
        valor = ' '
