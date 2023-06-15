from random import randint

numeros = list()


def somaPar(list):
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {list} temos {soma}')


def sorteia():
    cont = 0
    while True:
        n = randint(0, 10)
        if n not in numeros:
            numeros.append(n)
            cont +=1
        if cont == 5:
            break
    print(numeros)
    somaPar(numeros)


sorteia()
