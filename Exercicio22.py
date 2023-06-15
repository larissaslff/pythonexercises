nome=input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(' '))
nomes = nome.split()
print(len(nomes[0]))
print(nome.find(' ')) ## imprime a quantidade do 1 nome