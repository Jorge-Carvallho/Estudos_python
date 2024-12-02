# Exercício 09
# Faça um programa qu eleia um número inteiro informado pelo usuario,
# e mostre na tela a suia tabuada

numero = int(input('Digite o número para ver sua tabuada: '))
print(f'A tabuada do número {numero} é')
print('-'* 14)
print(f'{numero}  x  1  = {numero * 1}')
print(f'{numero}  x  2  = {numero * 2}')
print(f'{numero}  x  3  = {numero * 3}')
print(f'{numero}  x  4  = {numero * 4}')
print(f'{numero}  x  5  = {numero * 5}')
print(f'{numero}  x  6  = {numero * 6}')
print(f'{numero}  x  7  = {numero * 7}')
print(f'{numero}  x  8  = {numero * 8}')
print(f'{numero}  x  9  = {numero * 9}')
print(f'{numero}  x  10 = {numero * 10}')
print('-'* 14)

# obs: exemplo de outra forma 
print('---exemplo 2--')
print('{}  x  {}  = {}'.format(numero, 1 , numero*1))
print('{}  x  {}  = {}'.format(numero, 2 , numero*2))
print('{}  x  {}  = {}'.format(numero, 3 , numero*3))
print('{}  x  {}  = {}'.format(numero, 4 , numero*4))
print('{}  x  {}  = {}'.format(numero, 5 , numero*5))
print('{}  x  {}  = {}'.format(numero, 6 , numero*6))
print('{}  x  {}  = {}'.format(numero, 7 , numero*7))
print('{}  x  {}  = {}'.format(numero, 8 , numero*8))
print('{}  x  {}  = {}'.format(numero, 9 , numero*9))
print('{}  x  {}  = {}'.format(numero, 10 , numero*10))
print('-'* 14)