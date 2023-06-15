saque = float(input('Quanto vc quer sacar? '))
while True:
    de50 = int(saque/50)
    sub = de50 * 50
    saque -= sub
    de10 = int(saque/10)
    sub = de10 * 10
    saque -= sub
    de1 = int(saque/1)
    break
if de50 != 0:
    print(f'Total de {de50} cédulas de R$50')
if de10 != 0:
    print(f'Total de {de10} cédulas de R$10')
if de1 != 0:
    print(f'Total de {de1} cédulas de R$1')
