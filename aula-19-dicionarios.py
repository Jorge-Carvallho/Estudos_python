# pessoas = {'nome': 'Jorge', 'sexo': 'M', 'idade': 35}

# print(pessoas)
# print(pessoas['nome']) #mostra o indice nome o nome que esta no indice
# print(pessoas['idade']) #mostra a idade no indice idade
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# print(pessoas.keys()) #Mostra as chaves que na lista poderia ser os indices
# print(pessoas.values())#Mostra os valores das chaves
# print(pessoas.items()) #Mostra uma lista que contem  dicionários dentro
# print(len(pessoas)) #comprimento do dicionário
# for k in pessoas.keys(): # para cada chave in pessoa mostre k = chave
#     print(k)

# print('='*20)
    
# for v in pessoas.values(): # vai mostrar o valore de cada elemento da chave
#     print(v)
    
# for k, v in pessoas.items():# k referente a chave e v referente a valor  = pessoas.items()
#     print(f'{k}  =  {v}')
    
# del pessoas['sexo'] # excluir uma chave e junto o valor
# print('='*20)


# pessoas['nome'] = 'Leandro'# mudando o valor do nome
# print(pessoas)
# pessoas['Peso'] = 89 # adicionando uma keys()chave (peso) com values() valor (100)
# print(pessoas)
# print('='*20)

# #Adicionao um dicionário a uma lista
# brasil = []

# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla':'SP'}

# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)#dicionário dentro de uma lista chamada brasil
# print(brasil[0])# posição zero da lista brasil --> 1ª chave do dicionário
# print(brasil[1])# posição 1 da lista brasil --> 2ª chave do dicionário
# print(brasil[0]['uf'])
# print(brasil[1]['uf'])
# ---------------------------------------------------------------------------------------

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
#     for k, v in e.items():
    
#         print(f'O estado é {k} e a sigla é {v}')

# print(brasil)
        #  ou
    for v in e.values():
        print(v, end = ' ')
print()

