termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print(' PAUSA')
    mais = int(input('Quantos termos: '))
print('Progressão fianlizada com {} '.format(total))

