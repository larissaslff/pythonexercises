numero = int(input('Qual tabuada você deseja? '))

for c in range(0, 10 + 1):
    resultado = c * numero
    print('{} x {} = {}' .format(numero, c, resultado))