# Exercicio 85
# Crie um programa onde o usuário possa digitar sete valores
# numericos e cadastre-os em um alista única que mantenhaseparados os valores 
# pares e imparesem ordem crescente


# lista = [[],[]]
# for pos in range(1,8):
#     valor = int(input(f'Digite valor {pos}ª: '))
#     lista.append(valor)
# print('-='*25)

# print(f'Os valores pares foram, ',end='')
# for n in lista:
#     if n % 2 == 0:
#         print(n, end=' ')
# print()


# print(f'Os valores impares foram, ',end='')
# for n in lista:
#     if n % 2 != 0 :
#         print(n, end=' ')

# ------------------------------------------------------------------------------------------------
lista = [[],[]]

for pos in range(1,8):
    valor = int(input(f'Digite valor {pos}ª: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
        
print('-='*25)

print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores impares digitados foram {sorted(lista[1])}')
        
        