# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[2]) #--------> tuplas imutáveis

        #  ---------------------------
        
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi bem')

        # ------------------------------
        
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for cont in range(0, len(lanche)):
#     print(f'Hoje vou comer {lanche[cont]}')

# print('Comi bem')

      # ------------------------------
    #   enumerete ele mostra dando o dado quanto a posição
    

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for pos , comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Ufa')

    # -------------ordenando-----------------
    

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim','Batata frita')

# print(lanche)
# print(sorted(lanche))

a = (2,5,4)
b  = (5,8,1,2)
c = a + b
# print(sorted(c))
print(c)

# print(len(c))
# print(c.count(5))  #--> count() vai contar quantas vezes apareceu o número 5
print(c.index(4))   #--> index() quer saber em qual posição estar o número 8
print(c.index(2,3)) # --> mostra a primeira ocorencia do 2 aparti do indice 3 (deslocamento)

pessoa = ('Gustavo',39, 'M', 99.88)
del(pessoa) # apaga da memória a tupla pessoa
print(pessoa)

