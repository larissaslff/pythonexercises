lista = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper()[0]
        if resp in 'NS':
            break
        print('Apenas S/N')
    if resp == 'N':
        break
media = soma / len(lista)
print('-*' * 30)
print(f'A) Ao todo foram cadastradas {len(lista)} pessoas')
print(f'B) A média das idades é {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram:', end=' ')
for i in lista:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas acima da média: ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')