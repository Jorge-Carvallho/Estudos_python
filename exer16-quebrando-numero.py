# Exercício 16
# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a suaporção inteira.
# ex:..Digite um número 6.127.
# O número 6.127 tem a parte inteira 6. 
import math
valor_quebrado = float(input('Digite um valor: '))
valor_inteiro = math.trunc(valor_quebrado)

print(f'O valor digitado foi {valor_quebrado} e sua porção interira é {valor_inteiro}')