def leiaComando(msg):
    return help(msg)


while True:
    msg = str(input('Digite o comando: '))
    if msg == 'FIM':
        break
    leiaComando(msg)
