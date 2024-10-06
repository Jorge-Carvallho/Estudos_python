# Tuplas / imutáveis: o contéudo não pode ser alterado depois da declaração
# Tuplas são declaradas com parênteses ('a','b','c',)

tuplas = ('a','b','c')    # 2 tuplas concatenadas
tupla_nova = ('e','f','g')
print(tuplas + tupla_nova)

t = ('henrique')# str
t = ('henrique',)# deixa de ser uma str e vira uma tupla pois foi adicionado uma , ai final da str denttro do parêntese
print(tuple(t))# aqui trasforma uma str chamada t em uma tupla através do tuple()
print(t)
print('----------------------------------------')
t1 = ['1','2','3']# aqui ele é uma lista
print(tuple(t1)) # trasforma uma lista em uma tupla
print(tuple(t1[0]))# 3 posso acesar indices em uma tupla ou metodo slice com[:]
print(tuple(t1[1:3]))
print('-----------------------------------------')
#  A criação de uma tupla em Python é determinada pela presença da vírgula, e não apenas pelos parênteses. Os parênteses são usados para definir a ordem de precedência em expressões, mas a vírgula é o que efetivamente cria a tupla.
t2 = 'a','b','c','e',# t2 é um a tupla se eu precisasse concatenar t2 com outra tupla precisaria usar parêntese
print(t2)
t3 = ('h','u','j')+ t2 # t3 esta com parênteses
print(t3)
print('-------------------------------------------')
#tuplas vazias
tuple() 
t4 = ()
print(type(t4))
print('-----------------------------------------')
#Exercícios
#Crie duas tuplas chamadas tupla1 e tupla2 com os elementos ('a', 'b', 'c') e ('d', 'e', 'f') respectivamente.
# Concatene tupla1 e tupla2 e imprima o resultado.
#Crie uma tupla com um único elemento 'g' e imprima o tipo dela para confirmar que é uma tupla.
#Converta a string 'python' em uma tupla e imprima o resultado.
#Crie uma lista lista_exemplo com os elementos ['x', 'y', 'z'] e converta essa lista em uma tupla. Imprima a tupla resultante.
#Acesse e imprima o segundo elemento da tupla convertida.
#Faça um slice da tupla convertida para pegar os dois últimos elementos e imprima o resultado.
#Crie uma tupla vazia e imprima o tipo dela para confirmar que é uma tupla.

tupla1 = ('a','b','c')
tupla2 = ('d', 'e','f')

tupla_conectada = tupla1 + tupla2
print(tupla_conectada)
tupla_de_1_elemento = ('g',)#sem virgua é uma str, com virgula tuple
print(type(tupla_de_1_elemento))
tupla_string = 'Python'
print(tuple(tupla_string))
lista_exemplo = ['x','y','z']
print(tuple(lista_exemplo))
print(tuple(lista_exemplo[1]))
print(tuple(lista_exemplo[-2:]))
tupla_vazia = ()
print(type(tupla_vazia))