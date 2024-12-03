# Exercício 17
# Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.


# Triângulo Retângulo - Definições Básicas:
# Cateto Oposto:
# É o lado que está oposto ao ângulo que você está analisando.

# Se o ângulo está subindo à esquerda, o cateto oposto será a linha vertical.
# Cateto Adjacente:
# É o lado que está ao lado do ângulo que você está analisando (mas que não é a hipotenusa).

# Se o ângulo está subindo à esquerda, o cateto adjacente será a linha horizontal na base.
# Hipotenusa:
# É o lado mais longo do triângulo retângulo e está sempre oposto ao ângulo reto (90°).

# Neste caso, é a linha diagonal que conecta o topo do triângulo com a base.

#                                  .
#                                  ; . 
#                                  ;   .
#                                  ;      .------------> hipotenusa
#                                  ;        .
#         # cateto oposto  ----->  ;          . 
#                                  ;             .
#                                  ;---------------
#                                          !
#                                          v
#                                      cateto adjacente

import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacnete: '))

# hipotenusa = (cateto_oposto **2  + cateto_adjacente ** 2 ) ** 0.5
# print(f'A hipotenusa vai medir {hipotenusa:.2f}')

# ---------01--------usando métodos com import math---------------------------

# hipotenusa = pow(cateto_oposto,2) + pow(cateto_adjacente,2) 

# print(f'{math.sqrt(hipotenusa):.2f}')

# ---------02-------usando método da hipotenusa--------------------------------

hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
