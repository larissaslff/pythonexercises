sum = 0
h_mais_velho = ''
idade_h_mais_velho = 0
qtd_mulheres_menos20 = 0
for i in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: ' .format(i))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sum += idade
    sex = str(input('Digite o sexo (M, F) da {}ª pessoa: '.format(i)).upper()).strip()
    if sex == 'F' and idade < 20:
        qtd_mulheres_menos20 +=1
    if h_mais_velho == '' and sex == 'M':
        h_mais_velho = nome
        idade_h_mais_velho = idade
    if idade > idade_h_mais_velho and sex == 'M':
        idade_h_mais_velho = idade
        h_mais_velho = nome

    print('-' * 20)
print('A média do grupo é {:.2f}' .format(sum/4))
print('A quantidade de mulheres com menos de 20 é {}' .format(qtd_mulheres_menos20))
print('O homem mais velho é {} e tem {} anos' .format(h_mais_velho, idade_h_mais_velho))