'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par()
A primeria função vai sortear 5 números e vai colocar dentro da lista e a segunda função
vai mostrar a soma entre todos os valores Pares sorteados pela função anterios

'''


import random
numeros = [1,2,4,3]


sorteia = lambda lista:  random.choices(lista,k=5)
        #recebe uma lista e sorteia 5 números que é k=5

valores_sorteados = sorteia(numeros)
print(f'Números sorteados foi --> {valores_sorteados}')
        # os valores sorteados vinheram dos números 
        # sorteados do sorteia passando a lista1


soma_par = lambda valores_sorteados: sum(valor for valor in valores_sorteados if valor % 2 == 0)
        # recebe os valores sorteados, a função sum() ela calcula todos os elementos iteraveis
        # para cada valor de valores_sorteados se valor for par ele é somado


somar_pares = soma_par(valores_sorteados)
print(f'Soma dos números sorteados foi --> {somar_pares}')



assert soma_par([2]) == 2
assert soma_par([4]) == 4
assert soma_par([2,4]) == 6



     # acima usando funções lambda  ^
     # abaixo usando funções 
    
    

# import random

# numeros = [1,2,5,8,2,67,3]
# def sorteia(*valores):
#     quant_sort = 5  
#     valores_sorteados = random.choices(numeros, k=quant_sort)
#     valores = valores_sorteados
#     return valores


# def soma_par(n):
#     nova_list =[]
#     soma_pares = 0
#     for valor in n:
#         if valor % 2 == 0:
#             soma_pares += valor
                 
#     return soma_pares


# sorteia_numero = sorteia(numeros)
# print(f'Números sorteados foi --> {sorteia_numero}')
# somar_pares = soma_par(sorteia_numero)
# print(f'Soma dos números sorteados foi --> {somar_pares}')






