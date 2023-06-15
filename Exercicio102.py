def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} ' , end= '')
            if c > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
    #print(f'{f}')
    return f

print(fatorial(4))
