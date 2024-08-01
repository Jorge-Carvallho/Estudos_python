# Dicionários      declarado com {} dicionários não tem ordens
# para acessar a chave usa-se ['nome da cheve']

d = {'Nome': 'Henrique', 'Cidade': 'Salvador', 'Lat': 22.9, 'Long': 43.1}
print(d)
print(d['Nome']) #busca e imprime o valor da chave
d['Nome'] = 'Jorge Carvalho' #altera o contéudo da chave especificada
print(d)
print('asdf' in d)# verifica se existe uma chave em um dicionário ussar 'nome que pesquisa' in nome do dicionário retuna False ou True
print('jogando' in d.values())#verifica se existe o valor 'jogando' in d.values() (se existe o palavra jogando como valor no dicionário d) returna False ou True
print(d.get('asdf'))#verifica se existe a chave e returna None caso não existe ou returna o 2 parâmetro passado exemplo abaixo:
print(d.get('asdf','vamos criar'))# caso nao exista returna o valor passado no segundo parâmetro
print(len(d))#returna a quantidade de chaves
k = d.keys()
v = d.values()
i = d.items()
print(k)#returna apenas as chaves do dicionário
print(v)#retorna apenas os valores das chaves
print(i)#retorna os pares de chave e valor dentro de tuplas
# print(d['Nova-chave'] = 'valor-da-nova-chave')
d['ola'] = 'Nova-chave'
print(d) # os dicionário irar adicionar ao k,v,i as alteracoes
#Dicionário é donamico, tudo ele é alterado, porém posso trasforma ele em uma tupla ou lista exemplo abaixo:
# k = tuple(d.keys())
# v = tuple(d.values())
# i = tuple(d.items())
# print(k)              
# print(v)nesse bloco de código trasformo ele em uma tuple
# print('--------------------------------------------------')
