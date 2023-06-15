frase=str(input('Digite: ')).upper().strip()
print('A está {} vezes na frase' .format(frase.count('A')))
print('A está na {} posição na frase pela primeira vez' .format(frase.find('A') + 1))
ulltimo= frase.rfind('A') + 1
print(str(ulltimo))