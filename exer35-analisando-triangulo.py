# Exercício 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não forma um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima PODEM FORMA TRIÂNGULO!')
else:
    print('Os segmentos NÃO PODEM FORMA TRIÂNGULO!')
    