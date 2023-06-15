lista = []
for c in range(0,5):
    lista.append(int(input(f'Valor da Posição {c} : ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {maior} na posição {lista.index(maior) + 1}')
print(f'O maior valor foi {menor} na posição {lista.index(menor) + 1}')