def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO. Digite um número válido: ')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados encerrada pelo usuário!')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um número: '))
        except (ValueError, TypeError):
            print('ERRO')
        except (KeyboardInterrupt):
            print('Interrompido pelo usuário')
            return 0
        else:
            return n

n1 = leiaInt('Digite um n: ')
n2 = leiaFloat('Digite um n: ')
print(f'Você acabou de digitar o número inteiro {n1} e o real {n2}')

