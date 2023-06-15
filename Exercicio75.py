numerosdigitados = (int(input('Digite um número: ')),
                    int(input('Digite outro número: ')),
                    int(input('Digite mais um número: ')),
                    int(input('Digite o último número: ')))
print(f'Você digitou os valores {numerosdigitados}')
print(f'O valor 9 apareceu {numerosdigitados.count(9)}')
if 3 in numerosdigitados:
    print(f'O valor 3 foi digitado na {numerosdigitados.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares foram ', end='')
for n in numerosdigitados:
    if n % 2 == 0:
        print(n, end=' ')