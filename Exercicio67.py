while True:
    num = int(input('Quer ver a tabulada de qual valor? '))
    if num < 0:
        break
    print('-' * 40)
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 40)
print('------PROGRAMA ENCERRADO------')