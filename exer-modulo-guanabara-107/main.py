#Exercício
# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(),diminuir(),
# dobro(), e metade().
# Faça também um programa principal que importe esse módulo e use algumas dessas funções
            # -------------->obs<-----------------#
# caso queria importa so apenas algumas funcionalidades, colocar:
# from moeda import metade, dobro etc.. assim so importa o que é nescesario

import moeda

pre = float(input('Digite um preço: R$ '))
print(f' A metade do R${pre} é R${moeda.metade(pre)}')
print(f' O dobro de R${pre} é R${moeda.dobro(pre)}')
print(f' Aumentando 10% em cima de R${pre} temos R${moeda.aumentar(pre,10)}')
print(f' Reduzindo 20% em cima de R${pre} temos R${moeda.diminuir(pre,20)}')



                # ------>   este exercício foi completado no exer_modulo_108  <---------- #