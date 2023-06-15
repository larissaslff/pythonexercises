frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range (len(junto) -1, -1, -1):
    inverso += junto[c]
if junto == inverso:
    print('Palindromo')
else:
    print('Não é palindromo')