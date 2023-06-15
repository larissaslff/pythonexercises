def notas(*n, situ=False):
    s = {}
    s['qtd_notas'] = len(n)
    s['maior'] = max(n)
    s['menor'] = min(n)
    s['media'] = sum(n)/len(n)
    if situ:
        if s['media'] >= 7:
            s['situação'] = 'Boa'
        else:
            s['situação'] = 'BAD'
    return s

print(notas(10, 8, 6, situ=True))