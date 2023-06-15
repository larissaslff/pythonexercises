from utilidadesCev.dado import dado
from utilidadesCev.moeda import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 12)