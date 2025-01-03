pessoas = {'nome': 'Jorge', 'sexo': 'M', 'idade': 35}

print(pessoas)
print(pessoas['nome']) #mostra o indice nome o nome que esta no indice
print(pessoas['idade']) #mostra a idade no indice idade
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys()) #Mostra as chaves que na lista poderia ser os indices
print(pessoas.values())#Mostra os valores das chaves
print(pessoas.items()) #Mostra um alista que comtem dentro os dicionários