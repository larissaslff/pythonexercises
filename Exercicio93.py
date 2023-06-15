jogador={
    'nome':  str(input('Nome do jogador: '))
}
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols =[]
for i in range(0, qtd):
    ngols = int(input(f'Quantos gols na partida {i +1}: '))
    gols.append(ngols)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {qtd} partidas.')
for i, v in enumerate(gols):
    print(f'Na partida {i}, fez {v}')

