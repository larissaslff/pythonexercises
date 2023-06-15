salario=float(input('Digite o seu salario: '))
if salario>1250:
    novo=salario*1.1
else:
    novo=salario*1.15
print('O novo salario é de R$ {:.2f}' .format(novo))