sex = str(input('Qual o seu sexo? M ou F? ')).strip().upper()[0]
while sex not in 'MmFf':
    sex=str(input('Tente novamente: ')).strip().upper()[0]
print('FIM')