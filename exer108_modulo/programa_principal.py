# Exercício 108
# Adapte o código do desafio 107 criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado

import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)}, temos {moeda.moeda(moeda.metade(p))} reais')
print(f'O dobro de {moeda.moeda(p)}, temos {moeda.moeda(moeda.dobro(p))} reais ')
print(f'Aumentando {p} em 10%, temos {moeda.moeda(moeda.aumentar(p))} reais')
print(f'Reduzindo {p} em 13%, temos {moeda.moeda(moeda.reduzir(p))} reais')