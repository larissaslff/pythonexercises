from random import shuffle
aluno1=input('Digite o seu nome: ')
aluno2=input('Digite o seu nome: ')
aluno3=input('Digite o seu nome: ')
aluno4=input('Digite o seu nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(lista)