def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if idade > 18 and idade < 65:
       return "VOTO OBRIGATÓRIO"
    elif idade > 65 or 16 <= idade < 18:
        return 'VOTO OPCIONAL'
    elif idade < 16:
        return 'Não vota'

anonascimento = int(input('Em que ano você nasceu? '))
print(voto(anonascimento))