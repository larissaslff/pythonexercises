def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO. Digite um n válido: ')
        if ok:
            break
    return valor



n = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o número {n}')
