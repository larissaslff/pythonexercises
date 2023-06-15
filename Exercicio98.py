from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f > i:
        while f >= i:
            print(f'{i}', end=' ', flush=False)
            sleep(0.5)
            i += p
    elif f < i:
        while f <= i:
            print(f'{i}', end=' ', flush=False)
            sleep(0.5)
            i -= p
    print()
    print('*=' * 20)


#contador(1, 10, 1)
#contador(10, 0, 2)
print('Agora é a sua vez')
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)

