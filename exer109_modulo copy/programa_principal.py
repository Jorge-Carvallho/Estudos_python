# Exercício 109
# Modifique as Funções que foram criadas no desafio 107 para que elas aceiterm um parâmetro a mais
# informando se o valor retornado por eles vai ser ou não formatado pela função moeda()
# desenvolvida no desafio 108

import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)}, temos {moeda.metade(p, True)} reais')
print(f'O dobro de {moeda.moeda(p)}, temos {moeda.dobro(p,True)} reais ')
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.aumentar(p,10,True)} reais')
print(f'Reduzindo {moeda.moeda(p)} em 13%, temos {moeda.reduzir(p,13)} reais')