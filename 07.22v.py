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