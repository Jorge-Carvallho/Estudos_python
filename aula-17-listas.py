# Aula de listas

num = [2,5,9,2,3,]
# num[1] = 20
# print(num)
# num.append(7) # adiciona ao final da lista
# print(num)
# num.sort()  # coloca os números em ordem
# num.sort(reverse=True) # coloca os números me ordem decrecente
# print(f'Essa lista tem {len(num)} elementos') # tamanho da lista
# num.insert(2,0) # primerio é indice, dpois o número que vai inserir (tipo adicionar o 0 no indice 2) 
# num.pop() # sem pararametro ele remove o último valor
# num.pop(2) # remove o valor do indice 2 da lista
# num.insert(2,2)
# print(num)
# num.remove(2) # remove ele remove a primeira ocorrencia
# print(num)
# if 4 in num:
#     num.remove(4)
# else: 
#     print('Não achei o número 4')
# print(num)

# ---------------------------------------------------------

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)


# for v in valores:
#     print(f'Os valores que estão na lista são {v}') mostra cada valor da lista

# for c, v in enumerate(valores): # enumerete mostra o índice e o valor
#     print(f'No índice {c} tenho o valor {v}')
    
    # ----------------------------------------------------
    
# ler o valor do teclado do input

# valores = list()
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
    
    
# print(valores)

    #   ----------------------------------------------
    
    # LIGAÇAO DAS LISTAS
a = [2,3,4,7]
b = a
# print(f'Lista A {a}')
# print(f'Lista B {b}')
# b[2] = 8                     # adicionando 8 na lista (b) também altera a lista (a)
# print(f'Lista {a}')
# print(f'Lista {b}')


    # COPIA DAS LISTAS
a = [2,3,4,7]
b = a[:]      # neste caso (b) esta recebendo uma copia de (a)
b[2] = 20
print(f'Lista A {a}')
print(f'Lista B {b}')
    
