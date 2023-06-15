nota1=float(input('Digite a nota nº 1'))
nota2=float(input('Digite a nota nº 2'))
media=(nota1 + nota2)/2
if media < 5.0:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')