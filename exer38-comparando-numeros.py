# Exercício 38
# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
#     - o primerio valor oe maior que o segundo
#     - o segundo valor é maior que o primerio
#     - os dois valores sao iguais

n1 = int(input('Digite o primerio número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O primerio número {n1} é maior que o segundo número {n2}.')
    
elif n2 > n1:
    print(f'O segundo número {n2} é maior que o primeiro número {n1}.')

else: 
    print('Ambos os números sõa iguais.')

