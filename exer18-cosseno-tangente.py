# Exercício 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno,
# cosseno e tangente desse ângulo.


#                            --> seno
#                       ^
#               .    .  !  .    .
#          .            !          .45ª
#        .              !  -------!   .
#      .                !         !     .
#     .   --------------!-----------------.>
#     .              *  !               . cosseno
#      .                !               .
#        .              !             .
#          .            !          .
#               .    .  !  .    .


import math

angulo = float(input(f'Digite o ângulo que deseja: '))

angulo_radianos = math.radians(angulo)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'O ângulode {angulo} tem o Seno de {round(seno,2)}')
print(f'O ângulode {angulo} tem o Seno de {round(cosseno,2)}')  # posso formatar também com :.2f
print(f'O ângulode {angulo} tem o Seno de {round(tangente,2)}')
