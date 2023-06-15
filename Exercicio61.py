termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print(' FIM')
