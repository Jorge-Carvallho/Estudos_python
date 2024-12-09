# # Exercício 50
# # Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# # que foram pares, se o valor for impar, desconsidere
# soma = 0

# for c in range(1, 7):
#     num = int(input(f'Digite o numeros {c} diferentes: '))# aqui ele verifica os 6 numeros digitados 
#     #mostrado 1,2,3,etc...
#     soma += num# auqi faz a soma dos números digitados
    
# if soma % 2 == 0: # fora do loop do for, se  soma dos números for par ele mostra,
#     #caso contrário ele informa que é impa e mostra o número
#     print(f'A soma dos números foi par --> {soma}')
# # else:
#     # print(f' A soma dos 6 números foi impar ----> {soma}')
    
    
    # ---------------------------------ou-------------------------------------------------
    # correto usar a variavelde contagem
    
    
soma = 0
cont = 0

print('Digite 6 números inteiros')
for c in range (1,7):
    num = int(input(f'Número {c}: '))
    if num % 2 == 0:
        soma += num
        cont +=1


if soma % 2 == 0:
    print(f'A soma dos números foram {soma}')
else:
    print(f'Resultado da soma é impar {soma}')