# Exercício 52
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo
# num = int(input('Digite um número: '))
# cont = 0
# for c in range(2, num):
#     if num % c  == 0:
#         cont += 1
#         break

# if cont == 0 and num > 1:
#     print(f'O numero {num} é primo')
# else: 
#     print(f'O número {num}, não é primo')

# --------------------------------------resolução--------------------------------------


num = int(input('Digite um número: '))
for c in range(1,num+1):
    if num % c == 0:
        print('\033[34m',end='')
    else:
        print('\033[m',end='')
    print('{}'.format(c),end=' ')