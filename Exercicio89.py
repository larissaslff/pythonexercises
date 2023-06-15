alunos = []
while True:
    nome = str(input('Digite o nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome,[n1,n2], media])
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 40)
print(f'{"Nº.":<4} {"NOME":<10} {"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)
while True:
    aluno=int(input('Mostrar notas de qual aluno? 999 Para finalizar'))
    if aluno == 999:
        break
    print(f'Notas de {alunos[aluno][0]} são {alunos[aluno][1]}')
print('FINALIZANDO... VOLTE SEMPRE')