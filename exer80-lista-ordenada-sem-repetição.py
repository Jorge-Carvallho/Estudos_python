# Exercício 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastra-os em uma lista
# já na posição correta de inserção(sem usar o sort().
# No final mostre uma a lista ordenada na tela.




# lista = []

# for c in range(0,5):
#     n = int(input('Digite um número: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos,n)
#                 break
#             pos +=1
#             print(pos)


# print(pos, lista)








# -----------------------------------------------------------------------------------------

lista = []

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 :                     # se ele for o primeiro
        lista.append(n)      
        print('Adicionado ao final da lista...')      
    elif n > lista[-1]:             # se ele for maior que o último
        lista.append(n)
        print('Adicionado ao final da lista...')  
    
    else:
        pos = 0
        while pos < len(lista):     # enquanto pos for menor que o tamanho da lista e:
            if n <= lista[pos]:     # e se n for menor ou igual ao lista na posição (verificar s e o número é menor ou igual ao número que esta la lista) se ele for menor :
                lista.insert(pos,n) # insert(vai inserir o n na posição pos, o número n)
                print(f'Adicionado na posição {pos} da lista...')  
                break
            pos += 1 

  
print('-='* 30)
print(f'Os valores digitados em ordens foram{lista}')





 



        
