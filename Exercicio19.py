from random import choice
aluno1=input('Digite o seu nome: ')
aluno2=input('Digite o seu nome: ')
aluno3=input('Digite o seu nome: ')
aluno4=input('Digite o seu nome: ')
sorteado= choice([aluno1, aluno2, aluno3, aluno4])
print('Elemento sorteado é {}' .format(sorteado))