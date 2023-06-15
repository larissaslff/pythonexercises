pos = 0
times = ('BOTAFOGO', 'PALMEIRAS', 'FLUMINENSE', 'ATLETICO-MG',
         'CRUZEIRO', 'FLAMENGO', 'ATLETICO-PR', 'SAO PAULO', 'SANTOS')
print(f'Os cinco colocados: {times[:5]}')
print(f'Os ultimos 4 colocados: {times[-4:]} ')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'A posição do Flamengo é: {times.index("FLAMENGO") + 1}')