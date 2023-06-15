import random
x = random.randint(0,5)
chute=int(input('Qual o numero? '))
if x == chute:
    print('Você acertou')
else:
    print('Voce errou, o numero era {}' .format(x))