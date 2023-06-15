lista = []
impares = []
pares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2==0:
        pares.append(n)
    else:
        impares.append(n)
    cont=str(input('Queres continuar? '))
    if cont in 'Nn':
        break
print(f'A lista completa {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')
