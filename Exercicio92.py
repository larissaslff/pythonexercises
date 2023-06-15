#A pessoa se aposenta depois 35 anos de contribuição
from datetime import  date
pessoa = {
    'nome': str(input('Nome: ')),
    'anonasc': int(input('Ano de nascimento: ')),
    'CTPS': int(input('CTPS [0 se não possuir]: '))
}
if pessoa['CTPS'] != 0:
    pessoa['anocontr'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['idade'] = date.today().year - pessoa['anonasc']
    pessoa['aposentar'] =  pessoa['anocontr'] + 35 - pessoa['anonasc']

for k, v in pessoa.items():
    print(f'{k}: {v}')
