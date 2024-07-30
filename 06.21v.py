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






