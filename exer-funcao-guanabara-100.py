import random

numeros = [1,2,5,8,2,67,3]

def sorteia(*valores):
    quant_sort = 5  
    valores_sorteados = random.choices(numeros, k=quant_sort)
    valores = valores_sorteados
    return valores

def soma_par(n):
    nova_list =[]
    soma_pares = 0
    for valor in n:
        if valor % 2 == 0:
            soma_pares += valor
                 
    return soma_pares


sorteia_numero = sorteia(numeros)
print(f'Números sorteados foi --> {sorteia_numero}')

somar_pares = soma_par(sorteia_numero)
print(f'Soma dos números sorteados foi --> {somar_pares}')












# numero_sorteado = random.choices(numeros, k=quantidade_sorteio)

# print(numero_sorteado)