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

cont = 0
num =  int(input('Digite um número: '))
for c in range(1,num+1):    # para cada número de 1 até o proprio número digitado
    if num % c == 0: #se número fou divisivel pelo contador e o resultado é zero ele é divisivel
        print('\033[34m', end='') # os números que forem divisiveis ele mostra azul
    else:
        print('\033[m', end='')# os números nao divisiveis mostra normal
    print(c) # mostra o contador 