#listas        Lista são sequência mutáveis, podem sofrer alterações que alterão o estado interno delas. No python a lista podem armazenar qualquer tipo de objeto
lista = ['a','b','c']
print(type(lista))
lista.append('d') # adiciona um novo elemento
lista.sort(reverse=True)# lista de tras pra frente
lista.sort() # ela fica em ordem alfabetica
print(lista)
print(lista[1:3]) # posso acessar elementos de uma lista atravéz de indices
print('----------------------01--------------------------')
lista1 = lista[:]
lista2 = lista1
lista2.append('f')
print(lista1)
print(id(lista1), id(lista2))# variaveis/(nomes que referencian a mesma lista vão sofreralteraçoes pois estão referenciadas um a outra ----outro exemplo abaixo

def f(x):
    x.append(42)
    return x      # passei lista1 como referencia para chamada da função f, dentro da funcao f o lista1 foi acessado pelo valor x e adicionando 42 que também alterou a listas que estavam referenciadas, no resultado do print(ambas sofreram alteração)

print(f(lista1), lista2)
print('------------------02----------------------------')
# exemplo sem ser referenciado onde é criado uma copia resa dentro da funcão
def g(x):
    x = x[:]
    x.append(51)# dessa forma apenas lista1 esta sendo referenciada, lista 2 não sera alterada pois está fazendo uma copia rasa da lista1
    return x

print(g(lista1), lista2)
print(lista1)
print('--------------------------------------------')

#Exercícios
#Crie uma variável chamada minha_lista e atribua a ela a lista: ['x', 'y', 'z'].
minha_lista = ['x','y','z']

#Adicione o elemento 'w' à lista.
#Ordene a lista em ordem alfabética reversa.
#Reordene a lista em ordem alfabética normal.
#Imprima a lista completa.
#Faça um slice que capture e imprima os elementos do índice 1 ao 2 (inclusive).
#Crie uma cópia rasa da lista chamada copia_lista e adicione o elemento 'k' a essa nova lista.
#Verifique se minha_lista e copia_lista têm IDs diferentes.
#Crie uma nova lista chamada referencia_lista que aponte para minha_lista e adicione o elemento 'j'.
#Verifique se minha_lista e referencia_lista têm o mesmo ID.
#Crie uma função adiciona_elemento que recebe uma lista e um elemento como parâmetros, adiciona o elemento à lista e retorna a lista. Use essa função para adicionar o número 99 a minha_lista.
#Crie uma função adiciona_sem_referencia que recebe uma lista e um elemento como parâmetros, faz uma cópia rasa da lista, adiciona o elemento à cópia e retorna a cópia. Use essa função para adicionar o número 100 a minha_lista.

minha_lista.append('w')
print(minha_lista)
minha_lista.sort()
print(minha_lista)
print(minha_lista[1:3])
copia_lista = minha_lista[:]
copia_lista.append('k')
print(copia_lista)
print(id(minha_lista), id(copia_lista))
referencia_lista = minha_lista
referencia_lista.append('j')
print(referencia_lista)
print(id(minha_lista), id(referencia_lista))
def adiciona_elemento(lista, elemento):
    lista.append(elemento)
    return lista

print(adiciona_elemento(minha_lista, 99))

def adiciona_sem_referencia(lista,elemento):
    lista_copia = lista[:]
    lista_copia.append(elemento)
    return lista_copia

print(adiciona_sem_referencia(minha_lista, 100))
print(minha_lista)
    
    
print('-----------------------------------------------------------------------------')

# Crie uma variável chamada minha_lista e atribua a ela a lista: ['x', 'y', 'z'].
# Adicione o elemento 'w' à lista.
# Ordene a lista em ordem alfabética reversa.
# Reordene a lista em ordem alfabética normal.
# Imprima a lista completa.
# Faça um slice que capture e imprima os elementos do índice 1 ao 2 (inclusive).
# Crie uma cópia rasa da lista chamada copia_lista e adicione o elemento 'k' a essa nova lista.
# Verifique se minha_lista e copia_lista têm IDs diferentes.
# Crie uma nova lista chamada referencia_lista que aponte para minha_lista e adicione o elemento 'j'.
# Verifique se minha_lista e referencia_lista têm o mesmo ID.

minha_lista = ['x','y','z']
minha_lista.append('w')
print(minha_lista)
minha_lista.sort(reverse=True)
print(minha_lista)
minha_lista.sort()
print(minha_lista)
print(minha_lista[1:2])
copia_lista = minha_lista[:]
print(copia_lista)
copia_lista.append('k')
print(copia_lista)
print(id(copia_lista), id(minha_lista))
referencia_lista = minha_lista
referencia_lista.append('j')
print(id(referencia_lista), id(minha_lista))
# Crie uma função adiciona_elemento que recebe uma lista e um elemento como parâmetros, adiciona o elemento à lista e retorna a lista. Use essa função para adicionar o número 99 a minha_lista.

lista = []
def adiciona_elemento(x):
    lista.append(x)
    return lista
    
    
adiciona_elemento('99')
print(lista)
#  oouu
                         

def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista
    
minha_lista = adicionar_elemento(minha_lista,'99')
print(minha_lista)
# Crie uma função adiciona_sem_referencia que recebe uma lista e um elemento como parâmetros, faz uma cópia rasa da lista, adiciona o elemento à cópia e retorna a cópia. Use essa função para adicionar o número 100 a minha_lista.

def adiciona_sem_referencia(lista, elemento):
    lista_copia = lista[:]
    lista_copia.append(elemento)
    return lista_copia

nova_lista = adiciona_sem_referencia(minha_lista,'100')
print(minha_lista)
print(nova_lista)
print(id(minha_lista), id(nova_lista))

minha_lista = adiciona_sem_referencia(minha_lista, '101')
print(minha_lista)




listinha = []

def adiciona(x,elemento):
    x.append(elemento)
    return x

listinha = adiciona(listinha,'22')
print(listinha)


l = [1,2,3,[5,6,7]]
m = l[3:]
m.append(9)
print(m)
print(l)
