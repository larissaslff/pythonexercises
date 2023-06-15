numero = []
while True:
    numero.append(int(input('Digite um valor: ')))
    resp=str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Voce digitou {len(numero)} numeros')
numero.sort(reverse= True)
print(f'Em ordem decrescente {numero}')
if 5 in numero:
    print('O valor 5 faz parte')
else:
    print('Não tem 5')