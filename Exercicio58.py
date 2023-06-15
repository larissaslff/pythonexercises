import random
cont = 0
num = random.randint(0, 10)
print('Acabei de pensar em um número...')
chute = int(input('Qual o seu palpite? '))
while num != chute:
    if chute > num:
        chute = int(input('Você errou! Menos... : '))
    if chute < num:
        chute = int(input('Você errou! Mais... : '))
    cont +=1
print('Você acertou! Foram necessária {} chances' .format(cont))