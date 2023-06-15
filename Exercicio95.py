jogador = dict()
jogadores = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for i in range(0, part):
        partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    cont = str(input('Deseja continuar? S/N')).upper()[0]
    if cont == 'N':
        break
#print(f'{"cod":<2} {"nome":<10} {"gols":<5} {"total":>10}')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, j in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in j.values():
        print(f'{str(d)}:<15', end=' ')
print()
while True:
    busc = int(input('Mostrar dados de qual jogador? 999 p/ parar: '))
    if busc == 999:
        break
    if busc >= len(jogadores):
        print('Erro!!! Não existe jogados')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[busc]["nome"]}')
        for i, g in enumerate(jogador[busc]['gols']):
            print(f'No jogo {i + 1} fez {g} gols')
print('Volte sempre')


