termos = int(input('Quantos termos? '))
t1 = 0
t2 = 1
qt = 0
print('0 -> 1 -> ', end='')
while qt < termos - 2:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    qt +=1
print('FIM')