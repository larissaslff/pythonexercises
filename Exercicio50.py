s = 0
for c in range(0, 6):
    numero = int(input('Digite o número: '))
    if numero % 2 == 0:
        s += numero
print(s)