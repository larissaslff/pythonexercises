lista = []
while True:
    num =(int(input('Digite um valor? ')))
    if lista.count(num) == 0:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Você digitou os números {lista}')



