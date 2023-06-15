numero = qtd = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    qtd += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} e a soma entre eles foi {}'.format(qtd, soma))
