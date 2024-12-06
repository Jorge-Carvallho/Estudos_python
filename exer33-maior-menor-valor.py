# Exercício 33
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.


# n1 = int(input('Primerio valor: '))
# n2 = int(input('Segundo valor: '))
# n3 = int(input('Terceiro valor: '))

# if n1 <= n2 and n1 <= n3:
#     menor = n1
# elif n2 <= n1 and n2 <= n3:
#     menor = n2

# else: 
#     menor = n3

# if n1 >= n2 and n1 >= n3:
#     maior = n1
# elif n2 >= n1 and n2>= n3:
#     maior = n2
# else:
#     maior = n3
 


# print(f'o menor valor digiado foi {menor}')
# print(f'O maior valor digitado foi {maior}')


# ------------------------------------resolução------------------------------------



n1 = int(input('Primerio valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# verifica o menor número:
menor = n1          # considerando que inicia o n1 sendo menor, eu elimino um verificação
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verifica o maior número:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
    
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
