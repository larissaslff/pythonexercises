from random import randint
from time import sleep
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador= int(input('Qual opção deseja? '))
opcoes = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('Computador jogou {}' .format(opcoes[computador]))
print('Jogador jogou {}' .format(opcoes[jogador]))
print('---' * 15)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Computador ganhou')
elif computador == 1:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Computador ganhou')
elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empate')