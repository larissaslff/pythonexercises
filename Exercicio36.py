valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao=valor/(anos*12)
if prestacao > salario*30/100:
    print('Para pagar R${} em {} anos, a prestação é de R${:.2f}' .format(valor, anos, prestacao))
    print('Empréstimo Negado')
else:
    print('O valor da prestação será de {:.2f}' .format(prestacao))
    print('Emprestimo pode ser concedido')