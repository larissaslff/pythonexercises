continuar = True
num1=float(input('Digite o 1º número: '))
num2=float(input('Digite o 2º número: '))
while continuar:
    print('''[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa''')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        print('A soma de {} mais {} é {} ' .format(num1, num2, num2+num1))
    elif opcao == 2:
        print('A multiplicação de {} mais {} é {} ' .format(num1, num2, num2*num1))
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior do que {}' .format(num1, num2))
        elif num2 > num1:
            print('{} é maior do que {}' .format(num2, num1))
        else:
            print('Valores iguais')
    elif opcao == 4:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
    elif opcao == 5:
        print('Fim!')
        continuar = False