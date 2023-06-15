numero = qtd = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    qtd +=1
    soma += numero
print(f'A soma dos {qtd} valores foi {soma}')
