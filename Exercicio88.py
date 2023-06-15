sorteados = []
from random import randint
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
qtd = int(input('Quantos jogos você quer sortear? '))
print(f'SORTEADO {qtd} JOGOS')
for i in range(1, qtd + 1):
    print(f'Jogo {i}: ', end='')
    for n in range(0,6):
        sorteado = randint(1, 60)
        while sorteado in sorteados:
            sorteado = randint(1, 60)
        sorteados.append(sorteado)
        if n == 5:
            sorteados.sort()
            print(sorteados)
            sorteados.clear()
print(f'{"BOA SORTE":^30}')