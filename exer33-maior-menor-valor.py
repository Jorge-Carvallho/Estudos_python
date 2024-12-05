# Exercício 33
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.


n1 = int(input('Primerio valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2

else: 
    menor = n3

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2>= n3:
    maior = n2
else:
    maior = n3
 


print(f'o menor valor digiado foi {menor}')
print(f'O maior valor digitado foi {maior}')





