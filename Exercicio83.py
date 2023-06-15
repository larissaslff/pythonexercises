parenteses = []
exp = str(input('Digite a expressão: '))
for l in exp:
    if l == '(':
        parenteses.append(l)
    elif l == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(l)
            break
if len(parenteses) == 0:
    print('Sua expressão está válida')
else:
    print('Expressão inválida')
