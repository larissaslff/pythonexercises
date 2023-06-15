velocidade=float(input('Qual a velocidade do carro?'))
multa = (velocidade - 80) * 7
if velocidade>80:
    print('Voce foi multado em R$ {:.2f}' .format(multa))