#Exercício
# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(),diminuir(),
# dobro(), e metade().
# Faça também um programa principal que importe esse módulo e use algumas dessas funções
import moeda

num = float(input('Digite um valor: '))
print(f' O dobro de {num:g} é {moeda.dobro(num)}')
print(f' A metade do {num} é {moeda.metade(num)}')
print(f' Aumentando o número {num} em 40% o resultado é {moeda.aumentar(num)}')
print(f' Reduzindo o número {num} em 20% o resultado é {moeda.reduzir(num)}')



