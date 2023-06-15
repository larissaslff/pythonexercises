from random import randint
parounao = ''
cont = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
while True:
    valor = int(input('Diga o valor: '))
    pc = randint(0, 10)
    escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if (pc + valor) % 2 == 0:
        parounao = 'DEU PAR'
    else:
        parounao = 'DEU IMPAR'
    print('-' * 40)
    print(f'Você jogou {valor} e o computador {pc}. Total de {valor + pc}. {parounao}')
    print('-' * 40)
    if parounao.strip()[4] == escolha:
        print('VOCE VENCEU')
        cont +=1
    else:
        print('Voce Perdeu')
        print('=-' * 20)
        print(f'GAME OVER! Vc venceu {cont} vezes.')
        break
