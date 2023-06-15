preco=float(input('Qual o preço do produto: '))
print('FORMA DE PAGAMENTO ')
print('[1] a vista em dinheiro/cheque')
print('[2] a vista em cartao')
print('[3] 2x cartao')
print('[4] 3x ou mais no cartao')
opcao=int(input('Qual é a opção? '))
if opcao == 1:
    preco1 = preco - (preco * (10 / 100))
elif opcao == 2:
    preco1 = preco - (preco * (5 / 100))
elif opcao == 3:
    preco1 = preco
elif opcao == 4:
    preco1 = preco + (preco * (20/100))
print('O preço é R$ {:.2f}' .format(preco1))
