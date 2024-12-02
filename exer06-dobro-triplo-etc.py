# Éxercicio 06
# Crie um algoritimo que leia um número e mostre seu dobro,triplo, e raiz quadrada.
import math

n1 = int(input('Digite um número: '))
dobro = n1 * 2 
triplo  =  n1 * 3
raiz =  n1 ** (1/2) # math.sqrt(n1)



print(f'O dobro de {n1} é {dobro}')
print(f'O triplo de {n1} é {triplo}')
print(f'A raiz quadrada de {n1} é {raiz}')