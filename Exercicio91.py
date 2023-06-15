from random import randint
from operator import itemgetter

jogadores = {}
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
print(jogadores)
print('-' * 30)
ranking = list()
ranking = sorted(jogadores.items(),key=lambda item: item[1], reverse=True)
for i, v in enumerate(ranking):
    print(f' {i + 1}ª lugar: {v[0]} com {v[1]}')
