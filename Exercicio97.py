def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


txt = str(input('Digite o texto: '))
escreva(txt)