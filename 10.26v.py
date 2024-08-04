#Decisões e Expressôes Lógicas if/else
nome = 'Henrique'
for c in nome:
    # if c in ('e','i','u'): # As 3 formas estão corretas 
    # if c in 'eiu':
    if c == 'e' or c == 'i' or c == 'u':# caso tenha as letras da condição estou colocando elas em maiúsculas
        print(c.upper())
    elif c == 'q':# coloquei outra condição que caso tenha a letra (q) irar trocar po @
        print('@')
    else:
        print(c)
print('------------------------------------------------')
        
        
        
#No python tudo que for vazio ou 0 é falso, exemplos:
print(bool(0))
print('dicionário',{})# dicionario vazio é falso
print('tupla',())# tupla vazia é falso
print('lista',[])#  lista vazia é falso


# No and retorna o último avaliado 
True and 'abc'# retorna 'abc'
'abc' and True # retorna True 
False and 'abc'# qualquer verificação and que tenha False o retorno séra False

# No or retorna o primeiro avaliado
# O operador (or) umas das expressões tem que ser verdadeiro, ou seja caso apenas uma seja verdadeiro ele retorna
True or 'abc'# retorna True
'abc' or True# retorna abc
False or 'abc'# retorna abc //// aqui como a primeiro é falso ele vai conferir se a segunda é verdadeira e retorna caso seja
'abc' or False# retorna abc //// aqui a primerio ja é verdadeira então ele já retorna sem necessariamente avaliar a segunda
