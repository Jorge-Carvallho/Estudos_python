# Exercício 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções

from moeda import metade, dobro, aumentar, reduzir


p = float(input('Digite o preço: '))
print(f'A metade de {p}, temos {metade(p)} reais')
print(f'O dobro de {p}, temos {dobro(p)} reais ')
print(f'Aumentando {p} em 10%, temos {aumentar(p)} reais')
print(f'Reduzindo {p} em 13%, temos {reduzir(p)} reais')