total = demil = cont = preco = 0
maisbarato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisbarato = nome
    if preco > 1000:
        demil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total}')
print(f'Temos {demil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} que custa R${menor}')

