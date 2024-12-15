# Exercício 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial



# print('Digite um número para')
# n1 = int(input('Calcular o fatorial: '))

# f = 1 # fatorial iniciada de 1
# for c in range(n1, 0, -1):
#     f *= c
#     print(f'{c}x')
# print(f'Calculando {n1} ! {f}')
    
    
# ---------------------------------------------resolução ---------------------------------

# from math import factorial    # import fatorial de modulo math

# n = int(input('Digite o número: '))     # recebe número de usuário
# f = factorial(n)                        # f recebe fatorial de número digitado pelo usuário
# print(f'O fatorial de {n} é {f}')       # imforma na tela o fatorial de de número é --> resposta


# --------------------------------------------------------------------------------------------

# n = int(input('Digite um número: '))

# c = n
# f = 1
# print(f'Calculando {n}! = ',end='')
# while c > 0:
#     print(f'{c}',end=' ')
#     print(' x ' if c > 1 else ' = ', end='', )
#     f*=c
#     c -= 1 
# print(f)
    
    
    
# ---------------------teste---------------------------------------------    
    
n = int(input('Digite um número: '))
c = n
f =1
while c > 0:
    print(c,end=' ')
    
    f*=c
    c -= 1
print(f)