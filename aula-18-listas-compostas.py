# teste = list()
# teste.append('Jorge')
# teste.append(35)
# # print(teste)

# galera = list()
# galera.append(teste[:])   # para que não altere a primeria estrutura preciso fazer uma copia com [:]
# # print(galera)
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])    # para que não altere a primeria estrutura preciso fazer uma copia com [:]
# # print(galera)

# #  ----------------------------------------------------------------------------------------------

# galera = [['João', 35],['Ana', 33],['Joaquim', 13],['Maria', 45]]
  

# # print(galera)
# # print(galera[0])
# # print(galera[0][0])
# # print(galera[2][1])
#         # --------------------------------------ou---------------------------------
        
# for p in galera:
#     print(p) #nome e idade dentro da lista
# print('-'*20)   


# for p in galera:
#     # print(p[0],p[1]) #nome e idade na posição de cada pessoa/ p[posição 0] e p[posição [1]]
#     print(f'{p[0]} tem {p[1]} anos de idade')
# print('-'*20)
#     # -----------------------------------------------------------------------------------------
    
    
galera = list()
dados = list()
totalmaior = totalmenor = 0
for c in range(0,3):
    dados.append(input('Seu nome: '))
    dados.append(int(input('Sua idade: ')))
    galera.append(dados[:]) # não pode esquecer de criar uma copia de dados com [:]
    dados.clear()
print()
    
# print(galera)
for p in galera:
    # print(f'{p[0]} tem {p[1]} anos')
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalmaior +=1


    else:
        print(f'{p[0]} é menor de idade')
        totalmenor +=1


print()
print(f'Temos  {totalmaior} maiores de idades e {totalmenor} menores de idade')
    
    
    

    
