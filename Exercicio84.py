lista = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O menor é {men}Kg', end=' ')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O maior é {mai}Kg', end=' ')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')