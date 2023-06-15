#def maior(*n):
 #   maior = max(n)
  #  print(f'Foram informados {len(n)} valores')
   # print(f'O maior é {maior}')
def maior(*num):
    cont = maior = 0
    for n in num:
        print(f'{n}', end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont +=1
    print(f'Foram informados {cont} valores')
    print(f'O maior é {maior}')
maior(100, 4,20)
maior()